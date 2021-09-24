from django.test import TestCase
from ..models import SurveyQuestion, SurveyAnswer

class SurveyQuestionTest(TestCase):
    def setUp(self):
        SurveyQuestion.objects.create(
            surveyQuestion="Do you feel OK", surveyOptions=["Yes", "No"]
        )

    def test_survery_question(self):
        survey_question = SurveyQuestion.objects.get(name="Do you feel OK")
        self.assertEqual(
            survey_question.is_correct(), ""
        )