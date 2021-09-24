# DJANGO SURVEY API

## STACK
* language: Python3
* Framework: Django
* Database: MongoDB
* Database connector: Djongo
* Infrastructure: Docker and Docker Compose

## SOLUTION APPROACH
### Code
Django framework is used to build this API. Tests are also done with the Framework's test suite. Used Django models in such a way that creates 2 Mongo DB collections. ```SurveyQuestion``` to contain survey questions created and ```SurveyAnswer``` to contain answers provided and answers are linked to the questions using ```ForeignKey```. ```.env``` is used to store the application database secrets and other application related secrets. 

### Infrastructure
To achieve the requirement of persistent data solutions, the API and Database are seperated from each other within the same network. The API and database containers use persistent storage volume so Data is intact should the containers restart for any reason. Containers connect to each other using container names.
Database secrets have been set variables gotten from environment variables in both the code and Docker compose files. This is to help us achieve some form of security and could be improved on in production environments. 

## TESTING
* In order to run the tests for the application locally run ```python3 manage.py test```. This is also included in the docker build step to ensure only code that passed tests is built.

## DEPLOY SOLUTION
Before you deploy, kindly fill in the generic details in ```mongo-init.js``` and ```envsetup.sh``` to have the database details that you want.

### Using Docker Compose
* This solution is deployed using Docker compose. The Docker compose setup includes 2 separate containers which are Mongo DB container and Survey API container.
* To deploy solution run  ```./envsetup.sh``` to create the environment variables to be used by the Docker Compose file then ```docker-compose up --build -d``` to start the application.
* To destroy solution run  ```docker-compose down```

### Using CI - GitHub Actions
* ```test.yml``` - Pull Requests will Trigger tests
* ```deploy.yml``` - Merge to Master branch will deploy the API using Docker Compose since on a server. 

### Running locally
To run the code locally (out of docker)
* Test with ```python3 manage.py test```
* Start API with ```python3 manage.py runserver 0.0.0.0:8080```

## ACCESS API ENDPOINTS (LOCALLY)
To access the API, you can use PostMan or any other HTTP Client of your choice

* To create a survery question - make a ```POST``` request to http://localhost:8080/api/survey/createsurvey with the below JSON format as Body

```
{
    "surveyQuestion": "Survery Question",
}
```
Where  "surveyQuestion" is a string with the Survey question.
* To create a survery question options - make a ```POST``` request to http://localhost:8080/api/survey/createsurveyoptions with the below JSON format as Body

```
{
    "surveyQuestion": ID,
    "surveyOptions": ["Option1", "Option2", "...", "Option N"]
}
```
Where  "surveyQuestion" is the ID of the Survey question and "surveyOptions" are the available options to answer the Survey.
* To answer a survey - make a ```POST``` request to http://127.0.0.1:8080/api/survey/submitanswer with the below JSON format as Body
```
{
    "surveyAnswer": "Chosen Answer",
    "surveyQuestion": "Survey Question ID"
}
```
Where  "surveyAnswer" is a string with the Survey answer and "surveyQuestion" is the ID referencing the survey question answered. 
* To retrieve the results of a survey - make a ```GET``` request to http://127.0.0.1:8080/api/survey/getanswer/id. Where "id" is the Survey Question ID whose answers are to be revealed. The answers are shown in JSON. 
* To retrieve all survey questions options and view their ID and Options -  make a ```GET``` request to http://127.0.0.1:8080/api/survey/getsurveyoptions.
* To retrieve all survey questions to view their ID -  make a ```GET``` request to http://127.0.0.1:8080/api/survey/getsurveyquestions.
* Health Check - To continously check the application for uptime, make a ```GET``` request to http://127.0.0.1:8080/api/survey/health. This endpoint should return a 200 Status OK to show that the API is healthy.