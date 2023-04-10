"""The quiz-game programm."""
from os import getenv

from dotenv import load_dotenv
from psycopg2 import connect

MAX_LENGTH = 11
EXIT = 'exit'
load_dotenv()

PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')


def main():
    """Start quiz-game."""
    while True:
        print('Выбери сколько вопросов будет в викторине (максимум {0} вопросов): '.format(total_questions))
        user_input = input()
        if user_input == EXIT:
            print('Вы вышли изи викторины!')
            break
        if user_input.isdigit() and int(user_input) in range(1, total_questions + 1):
            cur.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT {0}'.format(user_input))
            questions = cur.fetchall()
            break
        else:
            print('Ошибка ввода. Введите число от 1 до {0}.'.format(total_questions))

    score = 0
    if user_input != EXIT:
        for currentt, question in enumerate(questions):
            if currentt == 0:
                print('Вопрос {0} из {1}'.format(currentt + 1, user_input))
            else:
                print('Вопрос {0} из {1}.'.format(currentt + 1, user_input), end=' ')
                print('Правильных ответов: {0}/{1}'.format(score, currentt))
            print(question[1])
            print('1. {0}\n2. {1}\n3. {2}\n4. {3}.'.format(question[2], question[3], question[4], question[5]))

            while True:
                user_answer = input('Введите номер правильного ответа или "exit" для выхода: ')
                if user_answer.lower() == EXIT:
                    break
                try:
                    user_answer = int(user_answer)
                    if user_answer < 1 or user_answer > 4:
                        raise ValueError
                    break
                except ValueError:
                    print('Некорректный ввод. Введите число от 1 до 4 или "exit" для выхода: ')

            if isinstance(user_answer, str) and user_answer.lower() == EXIT:
                print('Вы вышли из викторины!')
                break

            if user_answer == question[6]:
                print('Правильно!')
                score += 1
            else:
                print('Неправильно. Правильный ответ:', str(question[6]))

        print('Вы ответили правильно на {0} из {1} вопросов'.format(score, currentt))
        if currentt > 0:
            print('Ваша оценка: {0}%'.format(score / (currentt) * 100))


if __name__ == '__main__':
    conn = connect(dbname=PG_DBNAME, host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASSWORD)
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM questions')
    total_questions = cur.fetchone()[0]
    main()
