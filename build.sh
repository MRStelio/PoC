#!/bin/bash
#
docker build -t project -f docker_build/project/Dockerfile .
docker run \
--name project-test \
--rm \
-dit \
-v "$(pwd):/home/PoC" \
project:latest

docker exec project-test pip install -r requirements.txt

docker pull mysql:5.7.35
docker run \
-dit \
-p 10021:3306 \
-e MYSQL_ROOT_PASSWORD=123456789 \
-v "$(pwd)/database:/var/lib/mysql" \
--rm \
--name mysql \
mysql:5.7.35

> .env
echo DB_HOST=\"127.0.0.1\" >> .env
echo DB_USER=\"root\" >> .env
echo DB_PASSWORD=\"123456789\" >> .env
echo DB_USED=\"test\" >> .env
echo DB_PORT=\"10021\" >> .env