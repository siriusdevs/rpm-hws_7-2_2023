#!/bin/bash


docker run -d \
--name quiz_DB \
-p 5430:5432 \
-v $HOME/postgresql/quiz_DB:/var/lib/postgresql/quiz_DB \
-e POSTGRES_PASSWORD=123 \
-e POSTGRES_USER=app \
-e POSTGRES_DB=quizDB \
postgres

sleep 2

psql -h 127.0.0.1 -p 5430 -U app quizDB -f init.ddl
