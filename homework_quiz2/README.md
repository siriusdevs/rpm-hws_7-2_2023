# Quiz Game

## In order to launch a quiz game. You need to take a few steps.
## The first step is to execute these commands.

    git clone git clone https://github.com/siriusdevs/rpm-hws_7-2_2023
    git checkout krylova

## The second step. You need to go to the "homework_quiz2" folder. 
    cd homework_quiz2

## Create a container using this command. Fill in the database

    chmod +x init_db.sh
    ./init_db.sh 

## Third step. Сreate .env file.

    HOST=localhost
    DATABASE=postgres
    DB_USER=quiz
    PASSWORD=1234
    PORT=5444

## And the very last step! Just run the program.

    python3 quiz.py
  
