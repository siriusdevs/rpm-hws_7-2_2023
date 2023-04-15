HOST = '127.0.0.1'
PORT = 8003

# TEMPLATES
MAIN_TEMPLATE = 'cryptosite/templates/index.html'
COINS_TEMPLATE = 'cryptosite/templates/coins.html'
MARKET_OVERVIEW_TEMPLATE = 'cryptosite/templates/market-overview.html'

# PAGES
MARKET_OVERVIEW = '/overview'
COINS_INFO = '/coins'
MAIN = '/'
PAGES = MARKET_OVERVIEW, COINS_INFO

# DB
SELECT = 'SELECT * FROM {table}'
INSERT = 'INSERT INTO {table} ({attrs}) VALUES ({values})'
DELETE = 'DELETE FROM {table}'
UPDATE = 'UPDATE {table} SET {data}'
SELECT_ID = 'SELECT id FROM {table}'
GET_TOKEN = 'SELECT token FROM token WHERE username=\'{username}\''
COINS_ALL_ATTRS = ['id', 'token_name', 'approximate_price', 'status', 'listing_date']
COINS_REQ_ATTRS = ['token_name', 'status', 'listing_date']
POST_RESPONSE_URL = f'http://{HOST}:{PORT}{COINS_INFO}?id='

# HTTP CODES
OK = 200
NOT_FOUND = 404
FORBIDDEN = 403
BAD_REQUEST = 400
NOT_IMPLEMENTED = 501
INTERNAL_ERR = 500

# СODING
ENCODING = 'KOI8-R'

# COINS CONST
ETHBTC = 'ETHBTC'
BUSDUSDT = 'BUSDUSDT'
DOGEUSDT = 'DOGEUSDT'
COINS = {
    'ETHBTC': {'symbol': 'ETHBTC'},
    'BTCUSDT': {'symbol': 'BTCUSDT'},
    'BUSDUSDT': {'symbol': 'BUSDUSDT'},
    'ARBUSDT': {'symbol': 'ARBUSDT'},
    'MATICUSDT': {'symbol': 'MATICUSDT'},
}
BINANCE_API_URL = 'https://binance43.p.rapidapi.com/avgPrice?'

# HEADERS NAMES
BINANCE_API_HEADER = 'X-RapidAPI-Key'
HEADER_LENGTH = 'Content-Length'
HEADER_TYPE = 'Content-Type'

# DEBUG MESSAGES
COINS_MSG = 'BINANCE API get_overview error'
