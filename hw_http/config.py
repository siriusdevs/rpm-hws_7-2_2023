HOST = '127.0.0.1'
PORT = 8001

# TEMPLATES
MAIN_TEMPLATE = 'index.html'
CITIES_TEMPLATE = 'cities.html'
HOTELS_TEMPLATE = 'hotels.html'

# PAGES
HOTELS = '/hotels'
CITIES = '/cities'
MAIN = '/'
PAGES = HOTELS, CITIES

# db
SELECT = 'SELECT * FROM {table}'
INSERT = 'INSERT INTO {table} ({attrs}) VALUES ({values})'
DELETE = 'DELETE FROM {table}'
UPDATE = 'UPDATE {table} SET {data}'
SELECT_ID = 'SELECT id FROM {table}'
GET_TOKEN = "SELECT token FROM token WHERE username='{username}'"
CITIES_ALL_ATTRS = ['id', 'city', 'country', 'language', 'population']
CITIES_REQ_ATTRS = ['city', 'country']
POST_URL = f'http://{HOST}:{PORT}{CITIES}?id='

# HTTTP codes
OK = 200
NOT_FOUND = 404
FORBIDDEN = 403
BAD_REQUEST = 400
NOT_IMPLEMENTED = 501
INTERNAL_ERR = 500

# CODING
ENCODING = 'KOI8-R'

RAPID_API_HEADER = 'X-RapidAPI-Key'
HEADER_LENGTH = 'Content-Length'
HEADER_TYPE = 'Content-Type'

# debug messsages
HOTELS_MSG = 'RAPID API get_hotels'
