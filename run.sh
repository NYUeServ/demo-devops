#!/bin/bash

docker kill helloworld
docker build -t helloworld .
docker run -d -p 5000:5000 --name helloworld --rm helloworld