HOST = '127.0.0.1'
PORT = 8003

# TEMPLATES
MAIN_TEMPLATE = 'index.html'
ANIMALS_TEMPLATE = 'animals.html'
CATS_TEMPLATE = 'cats.html'

#PAGES
CATS = '/cats'
ANIMALS = '/animals'
MAIN = '/'
PAGES = CATS, ANIMALS

# db
SELECT = 'SELECT * FROM {table}'
INSERT = 'INSERT INTO {table} ({attrs}) VALUES ({values})'
DELETE = 'DELETE FROM {table}'
UPDATE = 'UPDATE {table} SET {data}'
SELECT_ID = 'SELECT id FROM {table}'
GET_TOKEN = 'SELECT token FROM token WHERE username=\'{username}\''
ANIMALS_ALL_ATTRS = ['id', 'kind', 'areal', 'fact']
ANIMALS_REQ_ATTRS = ['kind', 'areal', 'fact']
POST_RESPONSE_URL = f'http://{HOST}:{PORT}/{ANIMALS}?id='

# HTTTP co3des
OK = 200
NOT_FOUND = 404
FORBIDDEN = 403
BAD_REQUEST = 400
NOT_IMPLEMENTED = 501
INTERNAL_ERROR = 500

# CODING
ENCODING = 'KOI8-R'

# location consts
# TABLE_LOCATION = 'https://avatars.mds.yandex.net/i?id=25f4a90e77e3878c1292dab81be3c99c62213064-4935642-images-thumbs&n=13'
# REFRIGERATOR_LOCATION = 'https://avatars.mds.yandex.net/i?id=badc9d1b630b52410b9980b0138de333-5235138-images-thumbs&n=13'
# BENCH_LOCATION = 'https://vnru.ru/images/old/iblock/9b0/9b0112183619eef0781dec1a43104ba7.jpg'
# LOCATIONS = {
#     'table': TABLE_LOCATION,
#     'refrigerator': REFRIGERATOR_LOCATION, 
#     'bench': BENCH_LOCATION
# }

CATAAS_API_URL = 'https://cataas.com/cat?json=True'

# headers' names
CATAAS_API_HEADER = 'X-Requested-With'
HEADER_LENGTH = 'Content-Length'
HEADER_TYPE = 'Content-Type'

# # debug messsages
CATS_MSG = 'CATAAS API get_cat'