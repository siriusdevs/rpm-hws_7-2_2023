#!/bin/bash
export PGPASSWORD=123

docker run -d --name http_project -p 5442:5432  -v $HOME/postgresql/http_project:/var/lib/postgresql/http_project -e POSTGRES_PASSWORD=123 -e POSTGRES_USER=app -e POSTGRES_DB=http_db postgres

sleep 2

psql -h 127.0.0.1 -p 5442 -U app -d http_db -f init_db.ddl