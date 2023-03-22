# About project "QuizGame":
## This is a simple version of quiz written on Python that connects with database.

# How to start. First steps
    git clone https://github.com/siriusdevs/rpm-hws_7-2_2023

    git checkout kulgavykh

    cd quizgame

# Next step is creating Docker container and filling database
    run init_script.sh

### Then, you shoul fill the .env file
# .env
    HOST - database host

    DATABASE - database name

    DB_USER - database user

    PASSWORD - database password
    
    PORT - database port

### Now move to project directory
### Run server with command:
    python3 main.py
