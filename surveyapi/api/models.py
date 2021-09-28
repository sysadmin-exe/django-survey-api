from typing import Iterable
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.core.exceptions import ValidationError


#Model for Questions
class SurveyQuestion(models.Model):
    surveyQuestion = models.CharField(max_length=240)
    #surveyOptions = models.JSONField(default=None)
    CreatedAt = models.DateTimeField(default=timezone.now)

class SurveyOption(models.Model):
    surveyQuestion = models.ForeignKey(SurveyQuestion, on_delete=models.DO_NOTHING)
    surveyOptions = models.JSONField(default=None)
    CreatedAt = models.DateTimeField(default=timezone.now)

#Model for answers to survey questions
class SurveyAnswer(models.Model):
    surveyQuestion = models.ForeignKey(SurveyQuestion, on_delete=models.DO_NOTHING)
    surveyAnswer = models.CharField(SurveyOption.surveyOptions, max_length=240)
    CreatedAt = models.DateTimeField(default=timezone.now)