# __First step__
#### run the command

```
git clone https://github.com/pushkareva/rpm-hws_7-2_2023
```
```
cd rpm-hws_7-2_2023
```
```
git checkout pushkareva
```

# __Second step__

#### move to folder hw_quiz:

```
cd homework_quiz_fork
```


#### Create a docker container
###### change the access rights to the script:

```
chmod +x script.sh
```
###### run the file to fill the database:

```
./script.sh
```
# __Third step__
#### create .env file according to the example

```
PG_HOST=127.0.0.1
PG_PORT=5433
PG_USER=app
PG_PASSWORD=sirius
PG_DBNAME=quiz_db
```
# __Fourth step__

#### run main.py

```
python3 main.py
```