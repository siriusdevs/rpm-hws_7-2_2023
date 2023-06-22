#!/bin/bash
export PG_PASSWORD=sirius
docker run -d -p 36788:5432 --name quiz_game -e POSTGRES_USER=app -e POSTGRES_PASSWORD=sirius -e POSTGRES_DB=quiz_db postgres

sleep 2

psql -h 127.0.0.1 -p 36788 -U app -d quiz_db -f init_db.ddl