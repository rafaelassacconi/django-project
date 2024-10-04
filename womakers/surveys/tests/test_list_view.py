from django.test import TestCase
from ..models import Question
from django.urls import reverse

class QuestionListViewTest(TestCase):
    def setUp(self):
        Question.objects.create(text="Pergunta 1")
        Question.objects.create(text="Pergunta 2")
        self.question3_disabled = Question.objects.create(text="Pergunta 3", enabled=False)

    def test_view_url_accessible_by_path(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('question-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_the_correct_template(self):
        response = self.client.get(reverse('question-list'))
        self.assertTemplateUsed(response, 'surveys/question_list.html')

    def test_view_is_returning_only_enabled_questions(self):
        response = self.client.get(reverse('question-list'))
        questions = response.context['object_list']

        self.assertEqual(questions.count(), 2)
        self.assertNotIn(self.question3_disabled, questions)

    def test_view_is_returning_a_message_when_no_questions(self):
        Question.objects.all().update(enabled=False)

        response = self.client.get(reverse('question-list'))
        self.assertContains(response, "Não tem nenhuma pesquisa disponível no momento.")
