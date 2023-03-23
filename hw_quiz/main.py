"""Quiz on Python."""

from os import getenv

import psycopg2
from dotenv import load_dotenv

load_dotenv()

PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')

conn = psycopg2.connect(
    dbname=PG_DBNAME,
    host=PG_HOST,
    port=PG_PORT,
    user=PG_USER,
    password=PG_PASSWORD,
)
cur = conn.cursor()


def get_questions():
    """Extract a random question from the "questions" table in the database.

    Returns:
        The first question from the "questions" table in the database
    """
    cur.execute('SELECT * FROM questions')
    return cur.fetchall()


def view_question(question):
    """Show question.

    Args:
        question: A tuple representing the selected question.

    Returns: none.
    """
    print(question[1])
    print('1. {0}'.format(question[2]))
    print('2. {0}'.format(question[3]))
    print('3. {0}'.format(question[4]))
    print('4. {0}'.format(question[5]))


def check_answer(question, answer):
    """Check correct answer.

    Args:
        question: tuple
        answer: int user's choise.

    Returns: bool.
    """
    return answer == question[6]


def main():
    """Get answer to question."""
    questions = get_questions()
    for question in questions:
        view_question(question)
        answer = input('Введите вариант ответа (1-4): ')

        try:
            try_answer = int(answer)
        except Exception:
            print('Некорректный ввод. Вводите цифру от 1 до 4')
            continue
        if check_answer(question, try_answer):
            print('Угадали!')
        else:
            print('Неправильно! Надо было {0}'.format(str(question[6])))

        play_again = input('Хотите сыграть еще раз? (да/нет)')
        if play_again.lower() != 'да':
            break

    conn.close()


if __name__ == '__main__':
    main()
