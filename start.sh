#!/bin/bash

app="reminder-service"
docker build --tag ${app} . 
docker run -p 80:80 ${app}