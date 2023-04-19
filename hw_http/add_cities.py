from os import getenv

from dotenv import load_dotenv
from psycopg2 import connect

load_dotenv()

PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')

request = "INSERT INTO cities (city, country, language,  population) VALUES ('%s','%s','%s', %d)"

cities = [
    ('Moscow', 'Russia', 'Russian', 13097539),
    ('Irkutsk', 'Russia', 'Russian', 623869),
    ('Istanbul', 'Turkey', 'Turkish', 10895257),
    ('Barcelona', 'Spain', 'Spanish', 5664579),
    ('New York', 'USA', 'English', 19496810),
]


connection = connect(dbname=PG_DBNAME, host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASSWORD)
cursor = connection.cursor()

for city, country, language, population in cities:
    cursor.execute(request % (city, country, language, population))

connection.commit()
