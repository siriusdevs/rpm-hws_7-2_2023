# Quiz Game
---
## In order to launch a quiz game. You need to take a few steps.
---
## The first step is to execute these commands.

`git clone git clone https://github.com/siriusdevs/rpm-hws_7-2_2023`
`git checkout krylova`

--
## The second step. You need to go to the "homework_quiz2" folder. 
`cd homework_quiz2`

## Create a container using this command. And create a table in which your quiz will be. 
## Or you can take my quiz about the series "Sharp visors" ::))
`chmod +x init_db.sh`
`./init_db.sh `

## My quiz:
`create table quiz
(
    id    text,
    first_answer text,
    second_answer text,
    third_answer text,
    correct_answer text
);

insert into quiz (id, first_answer, second_answer, third_answer, correct_answer)
values ('Как звали скаковую лошадь Томаса Шелби?', '1)Быстрый лис', '2)Секрет Грейс', '3)Счастливчик Том', '2)Секрет Грейс'),
	('Как звали сына Томаса Шелби и Грейс?', '1)Джордж', '2)Чарли', '3)Джеймс', '2)Чарли'),
	('Как назывался паб, который принадлежал «Острым козырькам»?', '1)«Красная роза»', '2)«Черный лев»', '3)«Гаррисон»', '3)«Гаррисон»'),
	('Куда должно было отправиться украденное в первом сезоне оружие?', '1)Северную Ирландию ', '2)В Индию', '3)В Ливию', '1)Северную Ирландию '),
	('На Грейс был «Проклятый» . . . когда она была убита.', '1)Рубин', '2)Сапфир', '3)Бриллиант', '1)Рубин');

select *
from quiz;`

## Third step. Сreate .env file.

`HOST=localhost
DATABASE=postgres
DB_USER=quiz
PASSWORD=1234
PORT=5444`

## And the very last step! Just run the program.

`python3 quiz.py`