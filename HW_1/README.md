# this server needs:

## postgres databases
###### with tables: 
###### token (username text primary key, token uuid)
###### students (id integer generated always as identity not null primary key, fname text not null, lname text not null, sname text, group_ text not null, age int)
###### trees (id serial, tree text not null, height int, age int not null, yield int)
###### professors (id serial, fname text NOT NULL, patronymic text NOT NULL, lname text, subject text, age int)

## .env file with credentials:
###### postgres: PG_DBNAME, PG_HOST, PG_PORT, PG_USER, PG_PASSWORD
