import psycopg2
from dotenv import load_dotenv
from os import getenv


load_dotenv()

PG_DBNAME = getenv('PG_DBNAME')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_USER = getenv('PG_USER')
PG_PASSWORD = getenv('PG_PASSWORD')

conn = psycopg2.connect(dbname=PG_DBNAME, host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASSWORD)
c = conn.cursor()


def get_question():
    c.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 1')
    return c.fetchone()


def view_question(question):
    print(question[1])
    print("1. " + question[2])
    print("2. " + question[3])
    print("3. " + question[4])
    print("4. " + question[5])


def check_answer(question, answer):
    return answer == question[6]


def main():
    while True:
        question = get_question()
        view_question(question)
        answer = int(input("Введите вариант ответа (1-4): "))

        if check_answer(question, answer):
            print('Угадали!')
        else:
            print("Неправильно! Надо было " + str(question[6]))

        play_again = input("Хотите сыграть еще раз? (да/нет)")
        if play_again.lower() != "да":
            break
    conn.close()


if __name__ == "__main__":
    main()
