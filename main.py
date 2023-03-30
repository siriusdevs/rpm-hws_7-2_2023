import psycopg2
from dotenv import load_dotenv
from os import getenv

# подключение к базе данных PostgreSQL
load_dotenv()
conn = psycopg2.connect(
    dbname=getenv('PG_DBNAME'),
    user=getenv('PG_USER'),
    password=getenv('PG_PASSWORD'),
    host=getenv('PG_HOST'),
    port=getenv('PG_PORT')
)
# создание курсора
cur = conn.cursor()

# запрос для получения всех вопросов и ответов из базы данных
cur.execute('SELECT question, answer1, answer2, answer3, answer4, answer FROM quiz')

# сохранение результатов запроса в переменной
results = cur.fetchall()

# инициализация переменных счетчиков правильных и неправильных ответов
correct = 0
incorrect = 0


for id in results:
    # вывод вопроса и запрос ответа у пользователя
    print(f'{id[0]} \n1. {id[1]}\n2. {id[2]} \n3. {id[3]} \n4. {id[4]}')
    while True:
        user_answer = input('Введите номер правильного ответа (1-4), или нажмите "q" для выхода: ')
        if user_answer == 'q':
            break
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            break
        print('Некорректный ввод. Введите номер правильного ответа (1-4), или нажмите "q" для выхода')

    # если пользователь нажал 'q', выходим из цикла
    if user_answer == 'q':
        break

    # проверка ответа пользователя
    if int(user_answer) == int(id[5]):
        print('Правильно!')
        correct += 1
    else:
        print(f'Неправильно. Правильный ответ: {id[5]}')
        incorrect += 1

    # вывод результатов
    print(f'Правильных ответов: {correct} \nНеправильных ответов: {incorrect}\n')

cur.close()
conn.close()
