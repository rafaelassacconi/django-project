from datetime import date
from django.test import TestCase
from ..models import Question, Option, Vote

class QuestionTestCase(TestCase):

    def test_question_creation(self):
        question = Question.objects.create(text="Qual sua cor favorita?")

        self.assertEqual(question.text, 'Qual sua cor favorita?')
        self.assertEqual(question.created_at, date.today())
        self.assertTrue(question.enabled)

    def test_question_string(self):
        question = Question.objects.create(text="Qual sua cor favorita?")
        
        self.assertEqual(str(question), 'Qual sua cor favorita?')

    def test_question_total_votes_property(self):
        question = Question.objects.create(text="Qual sua cor favorita?")
        option1 = Option.objects.create(text="Branco", question=question)
        option2 = Option.objects.create(text="Preto", question=question)

        Vote.objects.create(option=option1)
        Vote.objects.create(option=option2)
        Vote.objects.create(option=option2)

        self.assertEqual(question.total_votes, 3)

class OptionTestCase(TestCase):

    def test_option_creation(self):
        question = Question.objects.create(text="Qual sua cor favorita?")
        option1 = Option.objects.create(text="Option 1", question=question)
        Option.objects.create(text="Option 2", question=question)

        self.assertEqual(option1.question, question)
        self.assertEqual(question.option_set.count(), 2)

class VoteTestCase(TestCase):

    def test_option_creation(self):
        question = Question.objects.create(text="Qual sua cor favorita?")
        option1 = Option.objects.create(text="Option 1", question=question)
        vote = Vote.objects.create(option=option1)

        self.assertEqual(vote.option, option1)
        self.assertEqual(vote.created_at, date.today())
