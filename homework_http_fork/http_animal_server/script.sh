#!/bin/bash
export PGPASSWORD=cat

docker run -d \
--name animals -p 32771:5432 \
-v $HOME/postgresql/http_homework:/var/lib/postgresql/http_homework \
-e POSTGRES_PASSWORD=cat \
-e POSTGRES_USER=lina \
-e POSTGRES_DB=animals_db \
postgres

sleep 2

psql -h 127.0.0.1 -p 32771 -U lina -d animals_db -f init_db.ddl
