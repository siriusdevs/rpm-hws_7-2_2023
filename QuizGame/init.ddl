CREATE TABLE if not exists questions (
    question_id INT primary key generated always as identity,
    question TEXT,
    answer_1 TEXT,
    answer_2 TEXT,
    answer_3 TEXT,
    correct_answer INT
);
insert INTO questions (question, answer_1, answer_2, answer_3, correct_answer)
values ('What word describes characters that can be moved in a Scratch program?', 'Sprite', 'Pixie', 'Goblin', 1),
	   ('Which of these is NOT a programming language?', 'Ruby', 'Python', 'Banana', 3),
	   ('How many types of windows does Python use?', 'One', 'Two', 'Three', 2),
       ('What do shell windows show in Python?', 'Programming output', 'IDLE', 'Code', 1),
       ('Which of these does NOT run using a computer program?', 'Bicycle', 'Rocket', 'Train', 1);