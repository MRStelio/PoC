#!/bin/bash

docker build -t project -f docker_build/project/Dockerfile .
#docker network create project_network
docker run \
--name project-test \
--rm \
--network project_network \
-dit \
-v "$(pwd):/home/PoC" \
project:latest

docker exec project-test pip install -r requirements.txt

docker run \
-dit \
-p 10021:3306 \
-e MYSQL_ROOT_PASSWORD=123456789 \
-v "$(pwd)/database:/var/lib/mysql" \
--rm \
--name mysql \
--network project_network \
mysql:5.7.35

chmod -R \777 database
db_container_ip=`docker network inspect project_network -f "{{range .IPAM.Config}}{{.Gateway}}{{end}}"`

> .env
echo DB_HOST=\"$db_container_ip\" >> .env
echo DB_USER=\"root\" >> .env
echo DB_PASSWORD=\"123456789\" >> .env
echo DB_USED=\"test\" >> .env
echo DB_PORT=\"10021\" >> .env
echo TESTDATA_URL_SOURCE=\"https://jsonplaceholder.typicode.com/users\" >> .env





