# Instruction for the project
### Initialization and installation
Write the following commands to prepare for the start:
```
git clone https://github.com/blinmakersha/HW_rpm_2_semestr

git checkout kulgavykh

cd rpm-hws_7-2_2023

cd CryproSite
```

Next step is:
```
python3 init.py
```
This command will install requirements for the project, such as moduls, docker container, database and .env file.

Now you can find "authorization.txt" file. This file containes authorization information for HTTP requests.

## Run server
You can run the server with this command:
```
python3 main.py
```

And then go to:
http://127.0.0.1:8003/
#
## HTTP Requests with Postman
### PUT, POST and DELETE requests. First, you need to be an authorized user
Open Postman and add:
In the **Headers**:
- In the Key field type **Authorization**
- In the Value field type **admin {token}**
Your token is in the "requirements/authorization.txt"

#### If you want to execute POST requests

- In URL field: http://127.0.0.1:8003/coins
- In Body tab: input raw JSON
**example**: {"token_name": "Grizz", "approximate_price" : 49.10, "status": "Upcoming", "listing_date": "2025-01-02"}

#### If you want to execute DELETE requests

- In URL field: http://127.0.0.1:8003/coins
- After **"?"** you specify what data you want to delete
**example**: http://127.0.0.1:8003/coins?id=5

#### If you want to execute PUT requests

- In URL field: http://127.0.0.1:8003/coins
- After **"?"** you specify what data you want to put
**example**: http://127.0.0.1:8003/coins?id=5
- In *Body* tab: input raw JSON
**example**: {"token_name": "Grizz", "listing_date": "2025-02-02"}