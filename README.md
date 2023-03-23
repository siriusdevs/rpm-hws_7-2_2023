# A Python quiz game that works with a database.

# Set up the project.

`docker run  -d \
        --name postgres_db2023 \
        -e POSTGRES_USER=sirius_2023 \
        -e POSTGRES_PASSWORD=change_me \
        -e PGDATA=/postgres_data_inside_container \
        -v ~/sirius_db_2023/postgres_data:/postgres_data_inside_container \
        -p 38746:5432 \
        postgres:15.1`

docker start postgres_db2023

psql -h 127.0.0.1 -p 38746 -U sirius_2023 -f init_db.ddl

# .env:
database name, host, port, passsword and user to connect 
- PG_HOST: postgresql host
- PG_PORT: postgresql port
- PG_USER: postgresql username
- PG_PASSWORD: postgresql password
- PG_DBNAME: postgresql dbname

# run:
    python3 main.py 
