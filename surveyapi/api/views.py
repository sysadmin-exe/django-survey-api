from django.http import response
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status, generics

from api.models import SurveyQuestion, SurveyAnswer, SurveyOption
from api.serializers import SurveyQuestionSerializer, SurveyAnswerSerializer, SurveyOptionSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
# API Method - Function that creates a survey question
def surveyCreateQuestion(request):
    if request.method == 'POST':
        survey_question_data = JSONParser().parse(request)
        surveyserializer = SurveyQuestionSerializer(data=survey_question_data)
        if surveyserializer.is_valid():
            surveyserializer.save()            
            return JsonResponse(surveyserializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(surveyserializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
# API Method - Function that creates a survey options
def surveyCreateOption(request):
    if request.method == 'POST':
        survey_option_data = JSONParser().parse(request)
        surveyserializer = SurveyOptionSerializer(data=survey_option_data)
        if surveyserializer.is_valid():
            surveyserializer.save()            
            return JsonResponse(surveyserializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(surveyserializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
# API method - Answer a survey with the given options - POST
def surveySubmitAnswer(request):
    if request.method == 'POST':
        survey_answer= JSONParser().parse(request)
        surveyserializer = SurveyAnswerSerializer(data=survey_answer)
        if surveyserializer.is_valid():
            surveyserializer.save()
            return JsonResponse(surveyserializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(surveyserializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# API Method - Function that gets all survey questions - GET
def surveyGetAllQuestions(request):
    if request.method == 'GET':
        survey = SurveyQuestion.objects.all() 
        survey_serializer = SurveyQuestionSerializer(survey, many=True)
        return JsonResponse(survey_serializer.data,safe=False)
    
@api_view(['GET'])
# API Method - Function that gets all options with survey question id - GET
def surveyGetAllOptions(request):
    if request.method == 'GET':
        survey = SurveyOption.objects.all() 
        survey_serializer = SurveyOptionSerializer(survey, many=True)
        return JsonResponse(survey_serializer.data,safe=False)
    
@api_view(['GET'])
# API method - Get all answers that has been submitted for a particular question ID - GET
def getSurveyAnswer(request, pk):
    survey_answers = SurveyAnswer.objects.filter(surveyQuestion_id=pk) 
    if request.method == 'GET':
        survey_answers_serializer = SurveyAnswerSerializer(survey_answers, many=True)
        return JsonResponse(survey_answers_serializer.data,safe=False)


@api_view(['GET'])
# API method - Health check
def getHealth(request):
    return JsonResponse({"Health": "Everything is OK"}, status=status.HTTP_200_OK)