from os import getenv
import psycopg2
from dotenv import load_dotenv
from time import sleep

load_dotenv()

PG_DBNAME = getenv('POSTGRES_DBNAME')
PG_HOST = getenv('POSTGRES_HOST')
PG_PORT = getenv('POSTGRES_PORT')
PG_USER = getenv('POSTGRES_USER')
PG_PASSWORD = getenv('POSTGRES_PASSWORD')

def main():
     
    connection = psycopg2.connect(
        dbname=PG_DBNAME,
        host=PG_HOST,
        port=PG_PORT,
        user=PG_USER,
        password=PG_PASSWORD,
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM questions')

    def start_quiz():
        print('Викторина "Кругозор"')
        answer = input('Готовы ли Вы начать игру (да/нет) :')
        if answer.lower() in ['да', 'yes']:
            print('Начнем!')
            sleep(0.5)
            return True
        elif answer.lower() in ['нет', 'no']:
            print('Жаль... Возвращайтесь, когда будете готовы.')
            return False
        else:
            connection.close()

    if start_quiz():
        quiz(cursor.fetchall())
    connection.close()

    
# def quiz(questions):
#     num = 0
#     score = 0

#     while num < len(questions):
#         question = questions[num]
#         print('{0}) {1}) {2}) {3}) {4})'.format(*question[1:6]))
#         right = question[6] # обновляем правильный ответ для текущего вопроса
#         inp = int(input('Введите номер: '))

#         try:
#             try_answer = int(inp)
#             if not isinstance(try_answer, int):                
#                 raise ValueError 
#             print('Введите число')
#         except ValueError:
#             print('Введите число')
#             continue

#         print('inp', inp, type(inp))
#         print('try_answer', try_answer, type(try_answer))
#         print('right', right, type(right))

#         if try_answer == int(right):
#             score += 1
#             print('Верно!', '\n')
#         else:
#             print(f'Неправильный ответ! Верный ответ: {right}\n')
#         num += 1
#         if num == len(questions):
#             print(f"Викторина подошла к концу, спасибо за участие, вы набрали {score}/{len(questions)} баллов!")
#             if input('Хотите сыграть еще раз? (да/нет): ').lower() == 'да':
#                 num = 0
#                 score = 0

def quiz(questions):    
    num = 0
    score = 0
    
    while num < len(questions):
        question = questions[num]
        print('{0}) {1}) {2}) {3}) {4})'.format(*question[1:6]))
        right = question[6]        
        inp = input('Введите номер: ')
        
        try:
            try_answer = int(inp)
                          
            if not isinstance(try_answer, int):
                raise ValueError
                
            if try_answer != int(right):
                print(f'Неправильный ответ! Верный ответ: {right}\n')            
            else:
                score += 1
                print('Верно!', '\n')
        except ValueError:
            print('Введите целое число!')
            continue
        
        num += 1
        if num == len(questions):
            print(f"Викторина подошла к концу, спасибо за участие, вы набрали {score}/{len(questions)} баллов!")
            
            if input('Хотите сыграть еще раз? (да/нет): ').lower() == 'да':
                num = 0
                score = 0
    
    
if __name__ == '__main__':
    main()