#!/bin/bash

DEPLOY_DIR="demo-devops"

cd $DEPLOY_DIR

sudo docker kill helloworld
sudo docker build -t helloworld .
sudo docker run -d -p 5000:5000 -v $WORKSPACE:/app --name helloworld --rm helloworld