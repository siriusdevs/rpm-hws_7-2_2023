"""Main file which runs the quiz."""
from os import getenv

import psycopg2
from dotenv import load_dotenv

load_dotenv()

HOST = getenv('HOST')
DATABASE = getenv('DATABASE')
DB_USER = getenv('DB_USER')
PASSWORD = getenv('PASSWORD')
PORT = getenv('PORT')


def main():
    """Use main function which runs the quiz."""
    conn = psycopg2.connect(
        host=HOST,
        dbname=DATABASE,
        user=DB_USER,
        password=PASSWORD,
        port=PORT,
    )

    cur = conn.cursor()    # курсор для выполнения запросов
    cur.execute('SELECT * FROM questions')
    questions = cur.fetchall()    # берем результат запроса

    for question in questions:
        print(question[1])
        print('1) {0}'.format(question[2]))
        print('2) {0}'.format(question[3]))
        print('3) {0}'.format(question[4]), '\n')
        user_answer = int(input('Type your answer (1-3): '))
        if user_answer == question[5]:
            print('The answer is correct!', '\n')
        else:
            print('Incorrect answer! The correct answer is:', str(question[5]), '\n')

    conn.close()


if __name__ == '__main__':
    main()
