from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from psycopg2 import connect
from dotenv import load_dotenv
from os import getenv
from config import *
from json import loads
from views import cats, animals, main_page, list_to_paragraphs
from requests import get

URL = 'https://cataas.com/cat'

load_dotenv()

PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')
YANDEX_KEY = getenv('YANDEX_KEY')


def get_data(query: dict, table: str) -> dict:
    global db_cursor
    db_cursor.execute(query_request(SELECT.format(table=table), query))
    animals = db_cursor.fetchall()
    return {
        'number': len(animals), 
        'rendered_animals': list_to_paragraphs(animals)
        }


def query_request(request: str, query: dict):
    if query:
        parts = []
        for key, value in query.items():
            if isinstance(value, int):
                parts.append(f"{key}={value}")
            else:
                parts.append(f"{key}='{value}'")
        return '{0} WHERE {1}'.format(request, ' AND '.join(parts))
    return request


def get_cat() -> dict:
    response = get(CATAAS_API_URL)
    if response.status_code != OK:
        print(f'{CAT_MSG} failed with status code: {response.status_code}')

    if response.status_code == OK:
        return response


def change_db(request: str):
    global db_cursor, db_connection
    try:
        db_cursor.execute(request)
    except Exception as error:
        print(f'change_db error: {error}')
        return False
    else:
        db_connection.commit()
        return bool(db_cursor.rowcount)

########### REST API

def get_id(table: str, query: dict):
    global db_cursor, db_connection
    try:
        db_cursor.execute(query_request(SELECT_ID.format(table=table), query))
    except Exception as error:
        print(f'db get_id error: {error}')
        return 0
    else:
        return db_cursor.fetchone()[0]

def is_int(value: any):
    return isinstance(value, int)

def db_insert(table: str, data: dict) -> bool:
    keys = list(data.keys())
    values = [data[key] for key in keys]
    attrs = ', '.join([str(key) for key in keys])
    values_str = ', '.join([f"{value}" if is_int(value) else f"'{value}'" for value in values])
    return change_db(INSERT.format(table=table, attrs=attrs, values=values_str))

def db_delete(table: str, data: dict):
    return change_db(query_request(DELETE.format(table=table), data))

def db_update(table: str, query: dict, data: dict):
    data = ', '.join([f"{key}={val}" if is_int(val) else f"{key}='{val}'" for key, val in data.items()])
    return change_db(query_request(UPDATE.format(table=table, data=data), query))

def is_valid_token(username: str, token: str) -> bool:
    global db_cursor
    db_cursor.execute(GET_TOKEN.format(username=username))
    answer = db_cursor.fetchone()
    if answer:
        return token == answer[0]
    return False
        

class CustomHandler(BaseHTTPRequestHandler):

    def get_query(self, possible_attrs: dict = {}) -> tuple:
        result = {}
        index = self.path.find('?')
        if index != -1 and index != len(self.path) - 1:
            query_parts = self.path[index + 1:].split('&')
            query = [part.split('=') for part in query_parts]
            for key, value in query:
                if value.isdigit():
                    result[key] = int(value)
                else:
                    result[key] = value
            if possible_attrs:
                for attr in result.keys():
                    if attr not in possible_attrs:
                        raise Exception(f'unknown attribute <{attr}>')
        return result

    def get_template(self) -> str:
        if self.path.startswith(ANIMALS):
            try:
                query = self.get_query(ANIMALS_ALL_ATTRS)
            except Exception as error:
                return BAD_REQUEST, str(error)
            else:
                return OK, animals(get_data(query, ANIMALS[1:]))
        elif self.path.startswith(CATS):
            try:
                query = self.get_query()
            except Exception as error:
                return BAD_REQUEST, str(error)
            else:
                return OK, cats()
        return OK, main_page()


    def do_GET(self):
        code, page = self.get_template()
        self.respond(code, page)

    def get_body(self, required_attrs: dict = {}) -> tuple:
        try:
            content_length = int(self.headers[HEADER_LENGTH])
        except ValueError:
            msg = f'error while trying to get {HEADER_LENGTH}'
            print(f'{__name__}: {msg}')
            raise Exception(msg)
        else:
            body = loads(self.rfile.read(content_length).decode(ENCODING))
            # проверим, все ли обязательные атрибуты на месте
            for attr in required_attrs:
                if attr not in body:
                    msg = f'required attribute <{attr}> is missing'
                    print(f'{__name__} error: {msg}')
                    raise Exception(msg)
            return body


    def make_changes(self):
        if self.path.startswith(ANIMALS):
            if self.command == 'POST':
                try:
                    body = self.get_body(ANIMALS_REQ_ATTRS)
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    if db_insert(ANIMALS[1:], body):
                        id = get_id(ANIMALS[1:], body)
                        if id: 
                            msg = f'{POST_RESPONSE_URL}{id}'
                            code = OK
                        else:
                            code = INTERNAL_ERROR
                            msg = 'id not found after POST'
                    else:
                        code = BAD_REQUEST
                        msg = 'FAIL'
            elif self.command == 'PUT':
                try:
                    body = self.get_body()
                    query = self.get_query(ANIMALS_ALL_ATTRS)
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    code = OK
                    msg = 'OK' if db_update(ANIMALS[1:], query, body) else 'FAIL'
            elif self.command == 'DELETE':
                try:
                    query = self.get_query(ANIMALS_ALL_ATTRS)
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    code = OK
                    msg = 'OK' if db_delete(ANIMALS[1:], query) else 'FAIL'
            else:
                code = NOT_IMPLEMENTED
                msg = 'Not implemented by server, available requests are GET, PUT, DELETE'
            return code, f'{self.command} {msg}'
        
        return NOT_FOUND, 'Content was NOT FOUND'
        
############## ошибка
    def respond(self, code: int, msg: str):
        self.send_response(code)
        self.send_header(HEADER_TYPE, 'text')
        self.end_headers()
        self.wfile.write(msg.encode(ENCODING))


    def check_auth(self):
        auth = self.headers.get('Authorization', '').split()
        if len(auth) == 2:
            username, token = auth[0], auth[1][1:-1]
            if is_valid_token(username, token):
                return True
        return False

    def process(self):
        if self.check_auth():
            code, msg = self.make_changes()
        else:
            code, msg = FORBIDDEN, 'Authorization was failed!'
        self.respond(code, msg)

    def do_POST(self):     # PUT -> POST
        self.process()

    def do_DELETE(self):
        self.process()

    def do_PUT(self):
        self.process()


if __name__ == '__main__':
    db_connection = connect(dbname=PG_DBNAME, host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASSWORD)
    db_cursor = db_connection.cursor()
    with ThreadingHTTPServer((HOST, PORT), CustomHandler) as server:
        server.serve_forever()
    # server.server_close()
    db_cursor.close()
    db_connection.close()