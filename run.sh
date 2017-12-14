#!/bin/bash

DEPLOY_DIR="demo-devops"

cd $DEPLOY_DIR

docker kill helloworld
docker build -t helloworld .
docker run -d -p 5000:5000 --name helloworld --rm helloworld