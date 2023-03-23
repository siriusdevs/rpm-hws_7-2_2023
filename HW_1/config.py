# pylint: skip-file
HOST = '127.0.0.1'
PORT = 8001

# TEMPLATES
MAIN_TEMPLATE = 'index.html'
STUDENTS_TEMPLATE = 'students.html'
CHUCK_TEMPLATE = 'chuck.html'
TREES_TEMPLATE = 'trees.html'
PROFESSORS_TEMPLATE = 'professors.html'

#PAGES
STUDENTS = '/students'
TREES = '/trees'
PROFESSORS = '/professors'
CHUCK = '/chuck'
MAIN = '/'
PAGES = MAIN, STUDENTS, TREES, PROFESSORS, CHUCK

# db
SELECT = 'SELECT * FROM {table}'
INSERT = 'INSERT INTO {table} ({attrs}) VALUES ({values})'
DELETE = 'DELETE FROM {table}'
UPDATE = 'UPDATE {table} SET {data}'
SELECT_ID = 'SELECT id FROM {table}' 
GET_TOKEN = 'SELECT token FROM token WHERE username=\'{username}\''
STUDENTS_ALL_ATTRS = ['id', 'fname', 'lname', 'sname', 'group_', 'age']
STUDENTS_REQ_ATTRS = ['fname', 'lname', 'group_']
PROFESSORS_ALL_ATTRS = ['id', 'fname', 'patronymic', 'lname', 'subject', 'age']
PROFESSORS_REQ_ATTRS = ['fname', 'patronymic']
TREES_ALL_ATTRS = ['id', 'tree', 'height', 'age', 'yield']
TREES_REQ_ATTRS = ['tree', 'age']
POST_STUD_RESP_URL = f'http://{HOST}:{PORT}{STUDENTS}?id='
POST_PROF_RESP_URL = f'http://{HOST}:{PORT}{PROFESSORS}?id='
POST_TREE_RESP_URL = f'http://{HOST}:{PORT}{TREES}?id='


# HTTP codes
OK = 200
CREATED = 201
NOT_FOUND = 404
FORBIDDEN = 403
BAD_REQUEST = 400
NOT_IMPLEMENTED = 501
INTERNAL_ERROR = 500

# CODING
ENCODING = 'KOI8-R'

# chuck norris' URL
CHUCK_API_URL = 'https://api.chucknorris.io/jokes/random'

# headers' names
HEADER_LENGTH = 'Content-Length'
HEADER_TYPE = 'Content-Type'

# debug messsages
CHUCK_MSG = 'CHUCK NORRIS API get_chucknorris'

# consts
TIMEOUT = 15
