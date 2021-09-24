from django.conf.urls import url, include
from api import views 
from api.views import *

urlpatterns = [ 
    url(r'^api/survey/createsurvey$', views.surveyCreateQuestion), #create a survey question - POST
    url(r'^api/survey/createsurveyoptions$', views.surveyCreateOption), #create a survey Options - POST
    url(r'^api/survey/getsurveyoptions$', views.surveyGetAllOptions), #get all options with respective question id - GET
    url(r'^api/survey/getsurveyquestions$', views.surveyGetAllQuestions), #get all survey questions - GET
    url(r'^api/survey/submitanswer$', views.surveySubmitAnswer), #answer a survey question - POST
    url(r'^api/survey/getanswer/(?P<pk>[0-9]+)$', views.getSurveyAnswer), #get all answers on a survey question -  GET
    url(r'^api/survey/health$', views.getHealth) #check health status- GET

]
