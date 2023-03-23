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
    """Use main function which connects to the database."""
    conn = psycopg2.connect(
        host=HOST,
        dbname=DATABASE,
        user=DB_USER,
        password=PASSWORD,
        port=PORT,
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM questions')
    game(cur.fetchall())
    conn.close()


def game(questions):
    """Use this function to run the quiz.

    Args:
        questions (tuple): all the information from the table

    Returns:
        False: in case of Error
    """
    points = 0
    for question in questions:
        print(question[1])
        print('1) {0}'.format(question[2]))
        print('2) {0}'.format(question[3]))
        print('3) {0}'.format(question[4]), '\n')
        try:
            user_answer = int(input('Type your answer (1-3): '))
        except Exception:
            print('You need to write only numbers. Game over.')
            return False
        if user_answer == question[5]:
            points += 1
            print('The answer is correct!', '\n')
        else:
            print('Incorrect answer! The correct answer is:', str(question[5]), '\n')

    if points > 1:
        print('Your result is: {0}. You win!'.format(points))
    else:
        print('Your result is: {0}. You lose..'.format(points))


if __name__ == '__main__':
    main()
