# About project "QuizGame":
## This is a simple version of quiz written on Python that connects with database.

# How to start. First steps
    git clone https://github.com/siriusdevs/rpm-hws_7-2_2023

    git checkout kulgavykh

    cd QuizGame

# Next step is creating Docker container and filling database
    chmod +x init_script.sh

    ./init_script.sh

### Then, you shoul fill the .env file
# .env
    HOST = 127.0.0.1

    DATABASE = quizDB

    DB_USER = app

    PASSWORD = 123
    
    PORT = 5430

### Now move to project directory
### Run server with command:
    python3 main.py
