#!/bin/bash
export PG_PASSWORD=123
docker run -d --name quiz_project -p 5436:5432  -v $HOME/postgresql/quiz_project:/var/lib/postgresql/quiz_project -e POSTGRES_PASSWORD=123 -e POSTGRES_USER=app -e POSTGRES_DB=quiz_db postgres

psql -h 127.0.0.1 -p 5436 -U app -d quiz_db -f init_db.ddl