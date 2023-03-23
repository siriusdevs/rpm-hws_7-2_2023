# __First step__

#### run the command
```
git clone https://github.com/arinapruzhinina/rpm-hws_7-2_2023/tree/main

git checkout pruzhinina
```

# __Second step__

#### Move to folder hw_quiz:
```
cd hw_quiz
```


#### Create a docker container
###### Change the access rights to the script:
```
chmod +x script.sh
```
###### Run the file to fill the database:
```
./sript.sh
```
# __Third step__
#### Create .env file according to the example

```
PG_HOST=127.0.0.1
PG_PORT=5436
PG_USER=app
PG_PASSWORD=123
PG_DBNAME=quiz_db
```
