HOST = '127.0.0.1'
PORT = 8001

# TEMPLATES
MAIN_TEMPLATE = 'index.html'
ANIMALS_TEMPLATE = 'animals.html'
CATS_TEMPLATE = 'cats.html'

#PAGES
ANIMALS = '/animals'
CATS = '/cats'
MAIN = '/'
PAGES = ANIMALS, CATS

# db
SELECT = 'SELECT * FROM {table}'
INSERT = 'INSERT INTO {table} ({attrs}) VALUES ({values})'
DELETE = 'DELETE FROM {table}'
UPDATE = 'UPDATE {table} SET {data}'
SELECT_ID = 'SELECT id FROM {table}'
GET_TOKEN = 'SELECT token FROM token WHERE username=\'{username}\''
ANIMALS_ALL_ATTRS = ['id', 'kind', 'areal', 'fact']
ANIMALS_REQ_ATTRS = ['kind', 'areal', 'fact']
POST_RESPONSE_URL = f'http://{HOST}:{PORT}{ANIMALS}?id='

# HTTTP codes
OK = 200
NO_CONTENT = 204
NOT_FOUND = 404
FORBIDDEN = 403
BAD_REQUEST = 400
NOT_IMPLEMENTED = 501
INTERNAL_ERROR = 500

# CODING
ENCODING = 'KOI8-R'


CATAAS_API_URL = 'https://cataas.com/cat'

# headers' names
CATAAS_API_HEADER = 'X-Requested-With'
HEADER_LENGTH = 'Content-Length'
HEADER_TYPE = 'Content-Type'

#debug messsages
CAT_MSG = 'CATAAS API get_cat'