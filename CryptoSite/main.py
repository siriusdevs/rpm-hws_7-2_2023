from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from psycopg2 import connect
from dotenv import load_dotenv
from os import getenv
from config import *
from json import loads
from views import overview, coins_data, main_page, list_to_paragraphs
from requests import get

load_dotenv()

PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')
BINANCE_KEY = getenv('BINANCE_KEY')


def get_data(query: dict, table: str) -> dict:
    global db_cursor
    db_cursor.execute(query_request(SELECT.format(table=table), query))
    coins = db_cursor.fetchall()
    table_data = [[str(elem) for elem in record] for record in coins]
    return {
        'number': len(table_data),
        'rendered_coins': list_to_paragraphs(table_data),
    }


def is_ins(instance: any):
    return isinstance(instance, int)


def query_request(request: str, query: dict):
    if query:
        parts = []
        for key, instance in query.items():
            if is_ins(instance):
                parts.append(f'{key}={instance}')
            else:
                parts.append(f"{key}='{instance}'")
        return '{0} WHERE {1}'.format(request, ' AND '.join(parts))
    return request


def get_overview(query: dict) -> dict:
    overview_data = {
        'current price': None,
        'symbol': 'ETHBTC',
    }
    response = get(BINANCE_API_URL, params=query, headers={BINANCE_API_HEADER: BINANCE_KEY})
    if response.status_code != OK:
        print(f'{COINS_MSG} failed with status code: {response.status_code}')
        return overview_data
    response_data = loads(response.content)
    if not response_data:
        print(f'{COINS_MSG} api did respond with empty content')
        return overview_data
    price = round(float(response_data.get('price')), 2)
    symbol = query.get('symbol')
    if not price:
        print(f'{COINS_MSG} api did not provide price data')
        return overview_data
    overview_data['current price'] = price
    overview_data['symbol'] = symbol
    return overview_data


def change_db(request: str):
    try:
        db_cursor.execute(request)
    except Exception as error:
        print(f'change_db error: {error}')
        return False
    db_connection.commit()
    return bool(db_cursor.rowcount)


def get_id(table: str, query: dict):
    global db_cursor, db_connection
    try:
        db_cursor.execute(query_request(SELECT_ID.format(table=table), query))
    except Exception as error:
        print(f'change_db error: {error}')
        return 0
    return db_cursor.fetchone()[0]


def db_insert(table: str, data: dict) -> bool:
    keys = list(data.keys())
    values = [data[key] for key in keys]
    attrs = ', '.join([str(key) for key in keys])
    values_str = ', '.join([
        f'{value}' if is_ins(value) else f"'{value}'"
        for value in values
    ])
    return change_db(INSERT.format(table=table, attrs=attrs, values=values_str))


def db_delete(table: str, data: dict):
    return change_db(query_request(DELETE.format(table=table), data))


def db_update(table: str, query: dict, data: dict):
    data = ', '.join([
        f'{key}={val}' if is_ins(val) else f"{key}='{val}'"
        for key, val in data.items()
    ])
    return change_db(query_request(UPDATE.format(table=table, data=data), query))


def is_valid_token(username: str, token: str) -> bool:
    db_cursor.execute(GET_TOKEN.format(username=username))
    answer = db_cursor.fetchone()
    if answer:
        return token == answer[0]
    return False


class CustomHandler(BaseHTTPRequestHandler):

    def get_query(self, good_attrs: dict = None) -> tuple:
        print(1)
        res = {}
        index = self.path.find('?')
        if index not in (len(self.path) - 1, -1):
            query_parts = self.path[index + 1:].split('&')
            query = [part.split('=') for part in query_parts]
            for key, instance in query:
                if instance.isdigit():
                    res[key] = int(instance)
                else:
                    res[key] = instance
            if good_attrs:
                for attr in res.keys():
                    if attr not in good_attrs:
                        raise Exception(f'unknown attribute <{attr}>')
        return res

    def get_template(self) -> str:
        if self.path.startswith(COINS_INFO):
            try:
                query = self.get_query(COINS_ALL_ATTRS)
            except Exception as error:
                return BAD_REQUEST, str(error)
            return OK, coins_data(get_data(query, COINS_INFO[1:]))
        elif self.path.startswith(MARKET_OVERVIEW):
            try:
                query = self.get_query()
            except Exception as error:
                return BAD_REQUEST, str(error)
            return OK, overview(get_overview(query))
        return OK, main_page()

    def get(self):
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
        if self.path.startswith(COINS_INFO):
            if self.command == 'POST':
                try:
                    body = self.get_body(COINS_REQ_ATTRS)
                except Exception as error:
                    code, msg = BAD_REQUEST, str(error)
                else:
                    if db_insert(COINS_INFO[1:], body):
                        id_user = get_id(COINS_INFO[1:], body)
                        code, msg = OK, f'{POST_RESPONSE_URL}{id_user}' if id_user else INTERNAL_ERR, 'id not found'
                    else:
                        code = BAD_REQUEST
                        msg = 'FAIL'
            elif self.command == 'PUT':
                try:
                    body, query = self.get_body(), self.get_query(COINS_ALL_ATTRS)
                except Exception as err:
                    code = BAD_REQUEST
                    msg = str(err)
                else:
                    code = OK
                    msg = 'OK' if db_update(COINS_INFO[1:], query, body) else 'FAIL'
            elif self.command == 'DELETE':
                try:
                    query = self.get_query(COINS_ALL_ATTRS)
                except Exception as err:
                    code = BAD_REQUEST
                    msg = str(err)
                else:
                    code = OK
                    msg = 'OK' if db_delete(COINS_INFO[1:], query) else 'FAIL'
            else:
                code = NOT_IMPLEMENTED
                msg = 'Not implemented by server, available requests are GET, POST, DELETE'
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
        
    def do_GET(self):
        self.get()


if __name__ == '__main__':
    db_connection = connect(dbname=PG_DBNAME,
                            host=PG_HOST,
                            port=PG_PORT,
                            user=PG_USER,
                            password=PG_PASSWORD,
                            )
    db_cursor = db_connection.cursor()
    with ThreadingHTTPServer((HOST, PORT), CustomHandler) as server:
        server.serve_forever()
    db_cursor.close()
    db_connection.close()
