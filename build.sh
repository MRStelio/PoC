#!/bin/bash

docker build -t project -f docker_build/project/Dockerfile .
docker run \
--name project-test \
--rm \
-dit \
-v "$(pwd):/home/PoC" \
project:latest

docker exec project-test pip install -r requirements.txt

#docker pull mysql:5.7.35
#docker run \
#-dit \
#-p 10021:3306 \
#-e MYSQL_ROOT_PASSWORD=123456789 \
#-v "$(pwd)/database:/home/PoC/database" \
#--name mysql \
#mysql:5.7.35