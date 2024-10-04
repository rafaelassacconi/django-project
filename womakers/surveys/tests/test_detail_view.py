from django.test import TestCase
from django.urls import reverse
from ..models import Question, Option
from ..forms import QuestionForm

class QuestionDetailViewTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(text="Qual sua cor favorita?")
        self.option_1 = Option.objects.create(question=self.question, text="Azul")
        self.option_2 = Option.objects.create(question=self.question, text="Verde")

    def test_view_context_contains_question(self):
        response = self.client.get(reverse('question-detail', args=[self.question.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['question'], self.question)

    def test_view_context_contains_question_form(self):
        response = self.client.get(reverse('question-detail', args=[self.question.pk]))
        form = response.context['form']

        self.assertIsInstance(form, QuestionForm)

    def test_title_is_being_displaying_in_template(self):
        response = self.client.get(reverse('question-detail', args=[self.question.pk]))

        self.assertContains(response, self.option_1.text)
    
    def test_options_is_being_displaying_in_template(self):
        response = self.client.get(reverse('question-detail', args=[self.question.pk]))

        self.assertContains(response, self.question.text)
