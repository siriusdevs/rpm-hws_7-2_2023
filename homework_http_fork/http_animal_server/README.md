# HTTP server with cats and animals
#### It is http server, where you can GET/POST/PUT/DELETE animals and watch cool cats from cataas.com

## Let's start

### 1. Do this command to clone my repo

```
git clone https://github.com/Linapush/homework_http_fork.git
```
```
cd http_animal_server
```
```
git checkout pushkareva
```
### 2. You need to move folder with name homework_http_fork.

```
cd homework_http_fork
```

### 3. You need to create a docker container. Follow this few steps.

```
chmod +x script.sh
```
```
./script.sh
```
### 4. Create .env file in this folder with this text.
```
PG_DBNAME=animals_db
PG_HOST=127.0.0.1
PG_PORT=32771
PG_USER=lina
PG_PASSWORD=cat
```
### 5. __Now you should do this command to fill the database:__

```
python3 add_animals.py
```

## Everything is ready to run the project. Do command:
```
python3 main.py
```
## And click the link: http://127.0.0.1:8001

---
#### After this command you will see the main page. You can choose which page to go to. 
---
### If you choose the page with name "animals", you will see different animals and some infromation about them, like kind, areal and fact. 

#### You can open Postman and try to do POST/PUT/DELETE requests. Folows this steps:

##### 1. To do POST you should:
* paste the url http://127.0.0.1:8001/animals
* in field "Headers" you should paste:
in field key paste: "Authorization",
in field value paste: "admin {fe705453-aec1-408b-af94-556910ca0651}"
* in field "Body" you must choose a raw(JSON) and paste json like that:
```
{
    "animal": "some animal", 
    "kind": "some kind of animal"
}
```
##### It is necessary to fill field to do POST request. If you want, you can  past full request with areal and fact. Example:
```
{
    "animal": "some animal", 
    "kind": "some kind", 
    "areal": "areal",
    "fact": "fact"   
}
```
##### After this command you will see a url with city id. You can press ctrl and click to the link. You will see your city.

 ##### 2. To do PUT you should:
* paste the url http://127.0.0.1:8001/animals?id=
after "=" you must to paste aninal id, witch you want to update.
* in field "Headers" you should paste:
in field key paste: "Authorization",
in field value paste: "admin {fe705453-aec1-408b-af94-556910ca0651}"
* in field "Body" you must choose a raw(JSON) and paste json like that:
```
{
    "animal": "some animal", 
    "kind": "some kind", 
    "areal": "areal",
    "fact": "fact"  
}
```
In this field you should write changes, that you want to do.
##### After this command you will see an updated city.

##### 3. To do DELETE you should:
* paste the url http://127.0.0.1:8001/animals?id=
after "=" you must to paste animal id, witch you want to update.
* in field "Headers" you should paste:
in field key paste: "Authorization",
in field value paste: "admin {fe705453-aec1-408b-af94-556910ca0651}"
---
### If you choose the page with name "cats", you can different cute cats from cataas.com.
