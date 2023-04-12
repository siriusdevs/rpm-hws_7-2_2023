import os
import stat
from psycopg2 import connect
from dotenv import load_dotenv


SH_FILE = 'requirements/init_script.sh'
END_FILE = 'requirements/authorization.txt'


if __name__ == '__main__':
    st = os.stat(SH_FILE)
    os.chmod(SH_FILE, st.st_mode | stat.S_IEXEC)
    os.system(f'./{SH_FILE}')

    load_dotenv()
    pg_dbname = os.getenv('PG_DBNAME')
    pg_host = os.getenv('PG_HOST')
    pg_port = os.getenv('PG_PORT')
    pg_user = os.getenv('PG_USER')
    pg_password = os.getenv('PG_PASSWORD')
    db_connection = connect(dbname=pg_dbname, host=pg_host, port=pg_port, user=pg_user, password=pg_password)
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT token FROM token where username='admin'")
    token = db_cursor.fetchone()
    db_cursor.close()
    db_connection.close()
    with open(END_FILE, 'wt') as user_inf:
        user_inf.write(f'AUTH DATABASE INFO: username: admin\ntoken: {token[0]}')
    print(f'In "{END_FILE}" you can find authorization info')
