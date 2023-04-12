"""A quiz game that works with a database."""

from os import getenv

import psycopg2
from dotenv import load_dotenv

load_dotenv()

HOST = getenv('HOST')
DATABASE = getenv('DATABASE')
DB_USER = getenv('DB_USER')
PASSWORD = getenv('PASSWORD')
PORT = getenv('PORT')


def datab():
    """Use this function to connect to the database."""
    conn = psycopg2.connect(
        host=HOST, dbname=DATABASE, user=DB_USER, password=PASSWORD, port=PORT,
    )

    cursor = conn.cursor()  # Он помогает выполнять SQL-запросы из Python
    cursor.execute('SELECT * FROM quiz')  # Получаем список всех пользователей
    quiz(cursor.fetchall())  # Вернуть все строки

    cursor.close()  # Закрываем курсор
    conn.close()  # Закрываем соединение


def quiz(rows):
    """Quiz.

    Args:
        rows(tuple): all information from the  table
    """
    just_answer, correct = [], []

    for row in rows:
        print(
            'Вопрос:\n{0}\n  {1}\n  {2}\n  {3}'.format(row[0], row[1], row[2], row[3]),
        )
        while True:
            input_answer = int(input('Введите ответ: '))
            if input_answer not in range(1, 4):
                print('\nТакого варианта ответа нет! Попробуйте еще раз!')
            else:
                break

        just_answer.append(input_answer)

    for row_ans in rows:
        correct.append(int(row_ans[4][:1]))

    count = 0

    for indx in range(5):
        if just_answer[indx] == correct[indx]:
            count += 1

    if correct == just_answer:
        print('Все ответы правильные!\n')
    else:
        print('К сожалению, вы ответили не на все вопросы!🙁😫😩🥺😭😭😭😭😭\nПопробуйте еще раз!')
        print('Правильных ответов {0}/5'.format(count))


datab()
