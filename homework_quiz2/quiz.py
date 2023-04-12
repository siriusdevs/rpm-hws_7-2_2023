"""Это игра-викторина, которая работает с базой данных."""

import psycopg2

try:
    conn = psycopg2.connect(
        host='localhost', port='5444', database='postgres', user='quiz', password='1234',
    )
except Exception:
    print('Не удается установить соединение с базой данных')

cursor = conn.cursor()  # Он помогает выполнять SQL-запросы из Python
cursor.execute('SELECT * FROM quiz')  # Получаем список всех пользователей
rows = cursor.fetchall()  # Вернуть все строки

cursor.close()  # Закрываем курсор
conn.close()  # Закрываем соединение

just_answer = []
correct = []
count = 0
answer = [1, 2, 3]

print('\nВикторина! Как хорошо вы знаете сериал "Острые Козырьки"!')
start = int(input('Хотите начать? 1 - да 2 - нет: '))

if start == 1:

    for row in rows:
        print(
            'Вопрос:\n{0}\n  {1}\n  {2}\n  {3}'.format(row[0], row[1], row[2], row[3]),
        )
        while True:
            input_answer = int(input('Введите ответ: '))
            if input_answer not in answer:
                print('\nТакого варианта ответа нет! Попробуйте еще раз!')
            else:
                break

        just_answer.append(input_answer)

    for row_ans in rows:
        row_ans = int(row_ans[4][:1])
        correct.append(row_ans)

    for indx in range(5):
        if just_answer[indx] == correct[indx]:
            count += 1

    if correct == just_answer:
        print('Все ответы правильные!\nВы хорошо знаете сериал "Острые козырьки"')
    else:
        print('К сожалению, вы плохо знаете сериал!\nПравильных ответов {0}/5'.format(count))

else:
    print('Очень жаль! 🙁😫😩🥺😭😭😭😭😭')
