CREATE TABLE IF NOT EXISTS quiz (
    id INTEGER PRIMARY KEY, 
    question TEXT, 
    answer1 TEXT, 
    answer2 TEXT, 
    answer3 TEXT, 
    answer4 TEXT, 
    answer TEXT
);
INSERT INTO quiz VALUES (1, 'Какого объекта нет на рабочем столе компьютера?', 'Панель задач', 'Корзина', 'Панель управления', 'Сетевое окружение', '3');
INSERT INTO quiz VALUES (2, 'Какая единица измерения не относится к измерению информации?', 'бит', 'герц', 'байт', 'бод', '2');
INSERT INTO quiz VALUES (3, 'Каких компьютеров не бывает?', 'планшетных', 'портфельных', 'карманных', 'портативных', '2');
INSERT INTO quiz VALUES (4, 'Какое количество информации потребуется для кодирования одного из 256 символов?', ' 8 байтов', '10 байтов', '1 байт', '1 бит', '3');
INSERT INTO quiz VALUES (5, 'Какого свойства информации не существует?', 'дискретность', 'результативность', 'детерминированность', 'турбулентность', '4');


UPDATE quiz SET answer = 3 WHERE id = 1;
UPDATE quiz SET answer = 2 WHERE id = 2;
UPDATE quiz SET answer = 2 WHERE id = 3;
UPDATE quiz SET answer = 3 WHERE id = 4;

