from os import getenv

from dotenv import load_dotenv
from psycopg2 import connect
from requests import get

from config import *
from views import hotels, cities, main_page, list_to_paragraphs
from json import loads
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

load_dotenv()

PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')
RAPID_KEY = getenv('RAPID_KEY')


def get_data(query: dict, table: str) -> dict:

    global db_cursor
    db_cursor.execute(query_request(SELECT.format(table=table), query))
    db_cities = db_cursor.fetchall()
    return {
        'number': len(db_cities),
        'rendered_cities': list_to_paragraphs(db_cities),
    }


def is_int(num: any):
    return isinstance(num, int)


def query_request(request: str, query: dict):
    if query:
        parts = []
        for key, value in query.items():
            if is_int(value):
                parts.append(f'{key}={value}')
            else:
                parts.append(f"{key}='{value}'")
        return '{0} WHERE {1}'.format(request, ' AND '.join(parts))
    return request


def get_hotels(query: dict) -> dict:
    if query:
        location = query.get('location')
    else:
        location = 'irkutsk'
        print(f'{HOTELS_MSG} failed to get location from query, defaults to irkutsk')
    headers = {
        RAPID_API_HEADER: RAPID_KEY,
    }
    url = f'https://hotels4.p.rapidapi.com/locations/search?query={location}'
    response = get(url=url, headers=headers)
    if response.status_code != OK:
        print(f'{HOTELS_MSG} failed with status code: {response.status_code}')
    response_data = response.json()

    if not response_data:
        print(f'{HOTELS_MSG} api did respond with empty content')
    fact = response_data.get('fact')
    if not fact:
        print(f'{HOTELS_MSG} api did not provide factual hotels data')

    return response_data['suggestions'][1]['entities']


def change_db(request: str):
    global db_cursor, db_connection
    try:
        db_cursor.execute(request)
    except Exception as error:
        print(f'change_db error: {error}')
        return False
    db_connection.commit()
    return bool(db_cursor.rowcount)


def get_id(table: str, query: dict):
    try:
        db_cursor.execute(query_request(SELECT_ID.format(table=table), query))
    except Exception as error:
        print(f'db get_id error: {error}')
        return 0
    return db_cursor.fetchall()[-1][0]


def db_insert(table: str, data: dict) -> bool:
    keys = list(data.keys())
    values = [data[key] for key in keys]
    attrs = ', '.join([str(key) for key in keys])
    values_str = ', '.join([f'{value}' if is_int(value) else f"'{value}'" for value in values])
    return change_db(INSERT.format(table=table, attrs=attrs, values=values_str))


def db_delete(table: str, data: dict):
    return change_db(query_request(DELETE.format(table=table), data))


def db_update(table: str, query: dict, data: dict):
    data = ', '.join([f'{key}={val}' if is_int(val) else f"{key}='{val}'" for key, val in data.items()])
    return change_db(query_request(UPDATE.format(table=table, data=data), query))


def is_valid_token(username: str, token: str) -> bool:
    db_cursor.execute(GET_TOKEN.format(username=username))
    answer = db_cursor.fetchone()
    if answer:
        return token == answer[0]
    return False


class CustomHandler(BaseHTTPRequestHandler):

    def get_query(self, possible_attrs: dict = None) -> tuple:
        result = {}
        index = self.path.find('?')
        if index not in (len(self.path) - 1, -1):
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
        if self.path.startswith(CITIES):
            try:
                query = self.get_query(CITIES_ALL_ATTRS)
            except Exception as error:
                return BAD_REQUEST, str(error)

            return OK, cities(get_data(query, CITIES[1:]))
        elif self.path.startswith(HOTELS):
            try:
                query = self.get_query()
            except Exception as error:
                return BAD_REQUEST, str(error)

            return OK, hotels(get_hotels(query))
        return OK, main_page()

    def do_GET(self):
        code, page = self.get_template()
        self.respond(code, page)

    def get_body(self, required_attrs: dict = None) -> tuple:
        try:
            content_length = int(self.headers[HEADER_LENGTH])
        except ValueError:
            msg = f'error while trying to get {HEADER_LENGTH}'
            print(f'{__name__}: {msg}')
            raise Exception(msg)
        body = loads(self.rfile.read(content_length).decode(ENCODING))
        if required_attrs:
            for attr in required_attrs:
                if attr not in body:
                    msg = f'required attribute <{attr}> is missing'
                    print(f'{__name__} error: {msg}')
                    raise Exception(msg)
        return body

    def make_changes(self):
        if self.path.startswith(CITIES):
            if self.command == 'POST':
                try:
                    body = self.get_body(CITIES_REQ_ATTRS)
                except Exception as error:
                    code, msg = BAD_REQUEST, str(error)
                else:
                    if db_insert(CITIES[1:], body):
                        rec_id = get_id(CITIES[1:], body)
                        code, msg = (OK, f'{POST_URL}{rec_id}') if rec_id else (INTERNAL_ERR, 'id not found')
                    else:
                        code = BAD_REQUEST
                        msg = 'FAIL'
            elif self.command == 'PUT':
                try:
                    body, query = self.get_body(), self.get_query(CITIES_ALL_ATTRS)
                except Exception as error:
                    code, msg = BAD_REQUEST, str(error)
                else:
                    code, msg = (OK, 'OK') if db_update(CITIES[1:], query, body) else (BAD_REQUEST, 'ERR')
            elif self.command == 'DELETE':
                try:
                    query = self.get_query(CITIES_ALL_ATTRS)
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    code, msg = (OK, 'OK') if db_delete(CITIES[1:], query) else (NOT_FOUND, 'FAIL')

            else:
                code = NOT_IMPLEMENTED
                msg = 'Not implemented by server, available requests are GET, PUT, DELETE'
            return code, f'{self.command} {msg}'
        return NOT_FOUND, 'Content was NOT FOUND'

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

    def do_POST(self):

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
    db_cursor.close()
    db_connection.close()
