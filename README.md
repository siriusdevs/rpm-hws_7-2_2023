# This is http_server with long awaited (for me) cats and animals.
## Firstly, you should execute commands:
```bash
    git clone https://github.com/siriusdevs/rpm-hws_7-2_2023

    git checkout puskareva

    cd homework_http_fork
```

## Secondly you need in Docker container and database

```bash
docker run -d \
--name animals_db \
-p :32771 \
-e POSTGRES_USER=lina \
-e POSTGRES_PASSWORD=cat \
-e POSTGRES_DB=animals \
postgres
```

```bash
psql -h 127.0.0.1 -p 32771 -U lina -d animals_db
``` 
password: cat

## Thirdly you need in .env file
# .env
POSTGRES_DB=animals_db
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=32771
POSTGRES_USER=lina
POSTGRES_PASSWORD=cat

# In the end in project directory:
# Run server with command:
    python3 main.py
