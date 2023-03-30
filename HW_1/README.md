# this server needs:

## postgres connection. CMDS:
###### docker run  -d --name hw -p 38748:5432 \
###### -v $HOME/h_w/postgres_data:/postgres_data_inside_container \
###### -e POSTGRES_USER=hw \
###### -e POSTGRES_PASSWORD=change_me \
###### -e PGDATA=/postgres_data_inside_container \
###### postgres:15.1

###### psql -h 127.0.0.1 -p 38748 -U hw

###### psql -h 127.0.0.1 -p 38748 -U hw -d -f init_db.ddl

## postgres databases
###### with tables: 
###### token (username text primary key, token uuid)
###### students (id serial not null primary key, fname text not null, lname text not null, sname text, group_ text not null, age int)
###### trees (id serial, tree text not null, height int, age int not null, yield int)
###### professors (id serial, fname text NOT NULL, patronymic text NOT NULL, lname text, subject text, age int)

## .env file with credentials:
###### postgres: PG_DBNAME, PG_HOST, PG_PORT, PG_USER, PG_PASSWORD
