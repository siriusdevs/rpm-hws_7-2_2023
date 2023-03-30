!/bin/bash

export PASSWORD=123

docker run -d \
 --name quiz \
 -p 5430:5432 \
 -e POSTGRES_PASSWORD=123 \
 -e POSTGRES_USER=quiz \
 -e POSTGRES_DB=quiz \
 postgres

sleep 2

psql -h 127.0.0.1 -p 5430 -U quiz quiz -f init.ddl