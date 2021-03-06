from django.db.models import fields
from rest_framework import serializers 
from api.models import SurveyQuestion, SurveyAnswer, SurveyOption

class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=SurveyQuestion
        fields=('id', 'surveyQuestion', 'CreatedAt')

class SurveyOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=SurveyOption
        fields=('id', 'surveyQuestion', 'surveyOptions', 'CreatedAt')

class SurveyAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=SurveyAnswer
        fields=('id','surveyQuestion', 'surveyAnswer', 'CreatedAt')
