#!/bin/bash

export PGPASSWORD=1234
docker run  -d 
	--name quiz 
	-e POSTGRES_USER=quiz 
	-e POSTGRES_PASSWORD=1234 
	-e PGDATA=/quiz_db  
	-v ~/Desktop/quiz_bd 
	-p 5444:5432 
	postgres:15.1

psql -h localhost -p 5444 -U quiz
psql -h 127.0.0.1 -p 38748 -U hw -d postgres -f init_db.ddl
