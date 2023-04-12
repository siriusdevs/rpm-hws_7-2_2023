#!/bin/bash

pip install -r requirements/requirements.txt

# create docker container
docker run -d \
--name crypto_server \
-p 5555:5432 \
-v $HOME/postgresql/crypto_server:/var/lib.postgresql/crypto_server \
-e POSTGRES_PASSWORD=123 \
-e POSTGRES_USER=valun \
-e POSTGRES_DB=CRYPTO_DB \
postgres
sleep 2

# mount all changes
export PGPASSWORD=123
psql -h 127.0.0.1 -p 5555 -U app CRYPTO_DB -f requirements/db_init.ddl

python3 requirements/setup_env.py