#!/bin/bash

delete_migrations(){
  local app=$1
  
  sudo find ./auxo_assesment/$app/migrations/* -delete
  sudo touch ./auxo_assesment/$app/migrations/__init__.py
}


while getopts c:a:d:f: options; do
  case $options in
      c) COMMAND=$OPTARG;;
      a) ARGS=$OPTARG;;
      d) DIR=$OPTARG;;
      f) FUNTION=$OPTARG;;

  esac
done

echo "COMMAND = $COMMAND; ARGS = $ARGS ; DIR = $DIR ; FUNTION = $FUNTION"

case $COMMAND in


  "install")
    echo "runing env..."
    touch .env
    cat .env_example > .env
    docker-compose build
    ;;

  "loaddata")
    echo "runing django makemigrations..."
    docker-compose run --rm django python manage.py makemigrations 
    echo "runing django migrate..."
    docker-compose run --rm django python manage.py migrate 
    echo "runing env..."
    echo "create super user... "
    echo "from django.contrib.auth import get_user_model ; User = get_user_model(); User.objects.create_superuser(username='admin', email='admin@admin.com', password='admin1234', )" | docker-compose run --rm django python manage.py shell 
    echo "load data from json"
    cat auxo_assesment/loaddata.py | docker-compose run --rm django python manage.py shell
    ;;

  "reset-env")
    echo "cleaning db..."


    echo "downing containers..."
    docker-compose down

    echo 'delete database: '
    sudo find db.sqlite3 -delete

    echo "deleting migrations files..."
    delete_migrations "users"
    delete_migrations "flights"
    delete_migrations "ping"

    echo 're-build containers : '
    docker-compose build


    echo "runing django makemigrations..."
    docker-compose run --rm django python manage.py makemigrations 
    echo "runing django migrate..."
    docker-compose run --rm django python manage.py migrate 
    echo "create super user... "
    echo "from django.contrib.auth import get_user_model ; User = get_user_model(); User.objects.create_superuser(username='admin', email='admin@admin.com', password='admin1234', )" | docker-compose run --rm django python manage.py shell 
    echo "load data from json"
    cat auxo_assesment/loaddata.py | docker-compose run --rm django python manage.py shell
    ;;

  "runserver")
    echo "runing env..."
    docker-compose up
    ;;
  "down")
    echo "downing containers..."
    docker-compose down
    ;;
  "build")
    echo "build containers..."
    docker-compose build
    ;;
  "test")
    echo "runing test..."
    if [[ $FUNTION != ''  ]]; then
      docker-compose run --rm django pytest $DIR -k $FUNTION
    else
      docker-compose run --rm django pytest $DIR
    fi
    ;;
  "makemigrations")
    echo "runing django makemigrations..."
    docker-compose run --rm django python manage.py makemigrations 
    ;;
  "migrate")
    echo "runing django migrate..."
    docker-compose run --rm django python manage.py migrate 
    ;;

  *)

    echo "command $COMMAND no found:"
    echo ""
    echo "The available commands:"
    echo ""

    echo -e "- reset-env"
    echo -e "- runserver"
    echo -e "- down"
    echo -e "- build"
    echo -e "- test"
    echo -e "- makemigrations"
    echo -e "- migrate"

esac






