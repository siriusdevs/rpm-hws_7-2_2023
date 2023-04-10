# this server needs:

## postgres connection. CMDS:
###### docker run  -d --name hw -p 38748:5432 \
###### -v $HOME/h_w/postgres_data:/postgres_data_inside_container \
###### -e POSTGRES_USER=hw \
###### -e POSTGRES_PASSWORD=change_me \
###### -e PGDATA=/postgres_data_inside_container \
###### postgres:15.1

###### psql -h 127.0.0.1 -p 38748 -U hw

###### psql -h 127.0.0.1 -p 38748 -U hw -d postgres -f init_db.ddl

## postgres databases
###### with table: 
###### questions (id SERIAL PRIMARY KEY, question_text TEXT, answer_1 TEXT, answer_2 TEXT, answer_3 TEXT, answer_4 TEXT, correct_answer INTEGER);

## .env file with credentials:
###### postgres: PG_DBNAME, PG_HOST, PG_PORT, PG_USER, PG_PASSWORD
