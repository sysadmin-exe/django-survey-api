#!/bin/bash

sleep 60
python3 surveyapi/manage.py makemigrations api  
python3 surveyapi/manage.py migrate api
python3 surveyapi/manage.py runserver 0.0.0.0:8080