"""Main process for server."""


from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from os import getenv
from json import loads
from dotenv import load_dotenv
from config import *
from psycopg2 import connect
from views import professors, students, trees, chuck, main_page, list_to_paragraphs
from requests import get

load_dotenv()

PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')
YAND_KEY = getenv('YANDEX_KEY')


def get_st_data(query: dict, table: str) -> dict:
    """
    Get students data from DB.

    Args:
        query: dict - query_req
        table: str - table_db

    Returns:
        dict - result of get_st_data
    """
    global db_cursor
    db_cursor.execute(query_request(SELECT.format(table=table), query))
    studentss = db_cursor.fetchall()
    return {
        'number': len(studentss),
        'rendered_students': list_to_paragraphs(studentss),
    }
    

def get_prof_data(query: dict, table: str) -> dict:
    """
    Get professor data from DB.

    Args:
        query: dict - query_req
        table: str - table_db

    Returns:
        dict - result of get_prof_data
    """
    global db_cursor
    db_cursor.execute(query_request(SELECT.format(table=table), query))
    professorss = db_cursor.fetchall()
    return {
        'number': len(professorss),
        'rendered_professors': list_to_paragraphs(professorss),
    }


def get_tree_data(query: dict, table: str) -> dict:
    """
    Get trees data from DB.

    Args:
        query: dict - query_req
        table: str - table_db

    Returns:
        dict - result of get_tree_data
    """
    global db_cursor
    db_cursor.execute(query_request(SELECT.format(table=table), query))
    treess = db_cursor.fetchall()
    return {
        'number': len(treess),
        'rendered_trees': list_to_paragraphs(treess),
    }


def query_request(request: str, query: dict) -> str:
    """
    Get full request from database.

    Args:
        request: str - db_request
        query: dict - query_req

    Returns:
        str - result of query_request
    """
    if query:
        parts = []
        for key, valuee in query.items():
            if isinstance(valuee, int):
                parts.append(f"{key}={valuee}")
            else:
                parts.append(f"{key}='{valuee}'")
        return '{0} WHERE {1}'.format(request, ' AND '.join(parts))
    return request


def get_chucknorris(query: dict) -> dict:
    """
    Get chucknorris joke from API.

    Args:
        query: dict - query_req

    Returns:
        dict - result of get_chucknorris
    """
    chucknorris_data = {
        'value': None,
    }
    response = get(CHUCK_API_URL, timeout=TIMEOUT)
    if response.status_code != OK:
        print('Failed to get Chuck Norris joke')
        return chucknorris_data
    response_data = loads(response.content)
    if not response_data or 'value' not in response_data:
        print('Failed to get Chuck Norris joke data')
        return chucknorris_data
    chucknorris_data['value'] = response_data['value']
    return chucknorris_data


def change_db(request: str) -> bool:
    """
    Change db data from request.

    Args:
        request: str - request_db

    Returns:
        bool - result of change_db
    """
    global db_cursor, db_connection
    try:
        db_cursor.execute(request)
    except Exception as error:
        print(f'change_db error: {error}')
        return False
    else:
        db_connection.commit()
        return bool(db_cursor.rowcount)


def get_id(table, query: dict):
    """
    Get sid data from DB table.

    Args:
        table: str - table_db
        query: dict - query_req

    Returns:
        None - result of get_id
    """
    global db_cursor, db_connection
    try:
        db_cursor.execute(query_request(SELECT_ID.format(table=table), query))
    except Exception as error:
        print(f'db get_id error: {error}')
        return 0
    else:
        return db_cursor.fetchone()[0]  # type: ignore


def is_int(valuee):
    """
    Get students data from DB.

    Args:
        valuee: any - check_value

    Returns:
        bool - result of isinstance value int
    """
    return isinstance(valuee, int)


def db_insert(table: str, dataa: dict) -> bool:
    """
    Insert data into DB.

    Args:
        table: str - table_db
        dataa: dict - data_db

    Returns:
        bool - result of db_insert
    """
    keys = list(dataa.keys())
    valuess = [dataa[key] for key in keys]
    attrs = ', '.join([str(key) for key in keys])
    values_str = ', '.join([f"{valuee}" if is_int(valuee) else f"'{valuee}'" for valuee in valuess])
    return change_db(INSERT.format(table=table, attrs=attrs, values=values_str))


def db_delete(table: str, dataa: dict) -> bool:
    """
    Delete data from DB.

    Args:
        table: str - table_db
        dataa: dict - data_db

    Returns:
        bool - result of db_delete
    """
    return change_db(query_request(DELETE.format(table=table), dataa))


def db_update(table: str, query: dict, dataa: dict) -> bool:
    """
    Update data in DB.

    Args:
        table: str - table_db
        query: dict - query_req
        dataa: dict - data_db

    Returns:
        bool - result of db_update
    """
    dataa = ', '.join([f"{key}={vl}" if is_int(vl) else f"{key}='{vl}'" for key, vl in dataa.items()])  # type:ignore
    return change_db(query_request(UPDATE.format(table=table, data=dataa), query))


def is_valid_token(username: str, token: str) -> bool:
    """
    Check for token's valid.

    Args:
        username: str - username
        token: str - token

    Returns:
        bool - result of is_valid_token
    """
    global db_cursor
    db_cursor.execute(GET_TOKEN.format(username=username))
    answer = db_cursor.fetchone()
    if answer:
        return token == answer[0]
    return False


class CustomHandler(BaseHTTPRequestHandler):
    """This is representation of not existing smth."""

    def get_query(self, possible_attrs: dict) -> tuple:
        """
        Get query request.

        Args:
            possible_attrs: dict - possible attributes

        Returns:
            tuple - result of get_query
        """
        resultt = {}
        index = self.path.find('?')
        if index != -1 and index != len(self.path) - 1:
            query_parts = self.path[index + 1:].split('&')
            query = [part.split('=') for part in query_parts]
            for key, valuee in query:
                if valuee.isdigit():
                    resultt[key] = int(valuee)
                else:
                    resultt[key] = valuee
            if possible_attrs:
                for attr in resultt.keys():
                    if attr not in possible_attrs:
                        raise Exception(f'unknown attribute <{attr}>')
        return resultt  # type: ignore

    def get_template(self) -> str:
        """
        Get template for server.

        Args:

        Returns:
            str - get_template
        """
        if self.path.startswith(STUDENTS):
            try:
                query = self.get_query(STUDENTS_ALL_ATTRS)  # type: ignore
            except Exception as error:
                return BAD_REQUEST, str(error)  # type: ignore
            else:
                return OK, students(get_st_data(query, STUDENTS[1:]))  # type: ignore
        elif self.path.startswith(PROFESSORS):
            try:
                query = self.get_query(PROFESSORS_ALL_ATTRS)  # type: ignore
            except Exception as error:
                return BAD_REQUEST, str(error)  # type: ignore
            else:
                return OK, professors(get_prof_data(query, PROFESSORS[1:]))  # type: ignore
        elif self.path.startswith(CHUCK):
            try:
                query = self.get_query({})
            except Exception as error:
                return BAD_REQUEST, str(error)  # type: ignore
            else:
                return OK, chuck(get_chucknorris(query))  # type: ignore
        elif self.path.startswith(TREES):
            try:
                query = self.get_query(TREES_ALL_ATTRS)  # type: ignore
            except Exception as error:
                return BAD_REQUEST, str(error)  # type: ignore
            else:
                return OK, trees(get_tree_data(query, TREES[1:]))  # type: ignore
        return OK, main_page()  # type: ignore

    def do_GET(self) -> None:
        """
        Get respond from server.

        Args:

        Returns:
        None - respond
        """
        code, page = self.get_template()
        self.respond(code, page)  # type: ignore

    def get_body(self, required_attrs: dict) -> tuple:
        """
        Get body for server.

        Args:
            required_attrs: dict - required attributes

        Returns:
            tuple - result of get_body
        """
        try:
            content_length = int(self.headers[HEADER_LENGTH])
        except ValueError:
            msg = f'error while trying to get {HEADER_LENGTH}'
            print(f'{__name__}: {msg}')
            raise Exception(msg)
        else:
            body = loads(self.rfile.read(content_length).decode(ENCODING))
            for attr in required_attrs:
                if attr not in body:
                    msg = f'required attribute <{attr}> is missing'
                    print(f'{__name__} error: {msg}')
                    raise Exception(msg)
            return body

    def make_changes(self):
        """
        Make changes in db from server.

        Args:

        Returns:
            any - result of make_changes
        """
        if self.path.startswith(STUDENTS):
            if self.command == 'POST':
                try:
                    body = self.get_body(STUDENTS_REQ_ATTRS)  # type: ignore
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    if db_insert(STUDENTS[1:], body):  # type: ignore
                        idd = get_id(STUDENTS[1:], body)  # type: ignore
                        if idd:
                            msg = f'{POST_STUD_RESP_URL}{idd}'
                            code = OK
                        else:
                            code = INTERNAL_ERROR
                            msg = 'id not found after POST'
                    else:
                        code = BAD_REQUEST
                        msg = 'FAIL'
            elif self.command == 'PUT':
                try:
                    body = self.get_body({})
                    query = self.get_body(STUDENTS_ALL_ATTRS)  # type: ignore
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    code = OK
                msg = 'OK' if db_update(STUDENTS[1:], query, body) else 'FAIL'  # type: ignore
            elif self.command == 'DELETE':
                try:
                    query = self.get_query(STUDENTS_ALL_ATTRS)  # type: ignore
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    code = OK
                    msg = 'OK' if db_delete(STUDENTS[1:], query) else 'FAIL'  # type: ignore
        elif self.path.startswith(PROFESSORS):
            if self.command == 'POST':
                try:
                    body = self.get_body(PROFESSORS_REQ_ATTRS)  # type: ignore
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    if db_insert(PROFESSORS[1:], body):  # type: ignore
                        idd = get_id(PROFESSORS[1:], body)  # type: ignore
                        if idd:
                            msg = f'{POST_PROF_RESP_URL}{idd}'
                            code = OK
                        else:
                            code = INTERNAL_ERROR
                            msg = 'id not found after POST'
                    else:
                        code = BAD_REQUEST
                        msg = 'FAIL'
            elif self.command == 'PUT':
                try:
                    body = self.get_body({})
                    query = self.get_body(PROFESSORS_ALL_ATTRS)  # type: ignore
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    code = OK
                msg = 'OK' if db_update(PROFESSORS[1:], query, body) else 'FAIL'  # type: ignore
            elif self.command == 'DELETE':
                try:
                    query = self.get_query(PROFESSORS_ALL_ATTRS)  # type: ignore
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    code = OK
                    msg = 'OK' if db_delete(PROFESSORS[1:], query) else 'FAIL'  # type: ignore
        elif self.path.startswith(TREES):
            if self.command == 'POST':
                try:
                    body = self.get_body(TREES_REQ_ATTRS)  # type: ignore
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    if db_insert(TREES[1:], body):  # type: ignore
                        idd = get_id(TREES[1:], body)  # type: ignore
                        print(idd) 
                        if idd:
                            msg = f'{POST_TREE_RESP_URL}{idd}'
                            code = CREATED
                        else:
                            code = INTERNAL_ERROR
                            msg = 'id not found after POST'
                    else:
                        code = BAD_REQUEST
                        msg = 'FAIL'
            elif self.command == 'PUT':
                try:
                    body = self.get_body({})
                    query = self.get_body(TREES_ALL_ATTRS)  # type: ignore
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    code = OK
                msg = 'OK' if db_update(TREES[1:], query, body) else 'FAIL'  # type: ignore
            elif self.command == 'DELETE':
                try:
                    query = self.get_query(TREES_ALL_ATTRS)  # type: ignore
                except Exception as error:
                    code = BAD_REQUEST
                    msg = str(error)
                else:
                    code = OK
                    msg = 'OK' if db_delete(TREES[1:], query) else 'FAIL'  # type: ignore
        else:
            code = BAD_REQUEST
            msg = "Uknown attribute requested"

        return code, msg

    def respond(self, code: int, msg: str):
        """
        Get respond from server.

        Args:
            code: int - code
            msg: str - message

        Returns:
            any - result of respond
        """
        self.send_response(code)
        self.send_header(HEADER_TYPE, 'text')
        self.end_headers()
        self.wfile.write(msg.encode(ENCODING))

    def check_auth(self):
        """
        Check auth on server.

        Args:

        Returns:
            bool: result of check auth
        """
        auth = self.headers.get('Authorization', '').split()
        if len(auth) == 2:
            username = auth[0]
            token = auth[1][1:-1]
            if is_valid_token(username, token):
                return True
        return False

    def process(self):
        """
        Do some process.

        Args:

        Returns:
            None - result of process
        """
        if self.check_auth():
            code, msg = self.make_changes()
        else:
            code, msg = FORBIDDEN, 'Authorization was failed!'
        self.respond(code, msg)

    def do_POST(self):
        """
        Post something in DB from server.

        Args:

        Returns:
            None - result of do_POST
        """
        self.process()

    def do_DELETE(self):
        """
        Delete something in DB from server.

        Args:

        Returns:
            None - result of do_DELETE
        """
        self.process()

    def do_PUT(self):
        """
        Put something in DB from server.

        Args:

        Returns:
            None - result of do_PUT
        """
        self.process()


if __name__ == '__main__':
    db_connection = connect(dbname=PG_DBNAME, host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASSWORD)
    db_cursor = db_connection.cursor()
    with ThreadingHTTPServer((HOST, PORT), CustomHandler) as server:
        server.serve_forever()
    db_cursor.close()
    db_connection.close()
