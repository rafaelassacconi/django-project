from django.test import TestCase
from ..models import Question, Option, Vote
from datetime import date

class QuestionTestCase(TestCase):

    def test_question_creation(self):
        question = Question.objects.create(text="Qual sua cor favorita?")

        self.assertEqual(question.text, 'Qual sua cor favorita?')
        self.assertEqual(question.created_at, date.today())
        self.assertTrue(question.enabled)

    def test_question_string(self):
        question = Question.objects.create(text="Qual sua cor favorita?")
        self.assertEqual(str(question), 'Qual sua cor favorita?')

class OptionTestCase(TestCase):

    def test_option_creation(self):
        question = Question.objects.create(text="Qual sua cor favorita?")
        option1 = Option.objects.create(text="Option 1", question=question)
        option2 = Option.objects.create(text="Option 2", question=question)

        self.assertEqual(option1.question, question)
        self.assertEqual(question.option_set.count(), 2)

class VoteTestCase(TestCase):

    def test_option_creation(self):
        question = Question.objects.create(text="Qual sua cor favorita?")
        option1 = Option.objects.create(text="Option 1", question=question)
        vote = Vote.objects.create(option=option1)

        self.assertEqual(vote.option, option1)
        self.assertEqual(vote.created_at, date.today())