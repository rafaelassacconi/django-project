from django.core.management.base import BaseCommand
from ...models import Question, Option
from django.contrib.auth.models import Group, User

class Command(BaseCommand):
    help = "Create questions for test"

    def handle(self, *args, **options):

        Group.objects.create(name="Autor")
        Group.objects.create(name="Editor")

        question = Question.objects.create(text="Qual é o seu animal favorito?")
        Option.objects.create(question=question, text="Gato")
        Option.objects.create(question=question, text="Cachorro")
        Option.objects.create(question=question, text="Cavalo")

        question = Question.objects.create(text="O que você mais gostou de aprender com Django?")
        Option.objects.create(question=question, text="Models")
        Option.objects.create(question=question, text="Views")
        Option.objects.create(question=question, text="Templates")
        Option.objects.create(question=question, text="Migrations")

        question = Question.objects.create(text="Qual framework Python você achou mais fácil de aprender?")
        Option.objects.create(question=question, text="Flask")
        Option.objects.create(question=question, text="Fast API")
        Option.objects.create(question=question, text="Django")

        question = Question.objects.create(text="Qual será o seu próximo curso da WoMakersCode?")
        Option.objects.create(question=question, text="Agile")
        Option.objects.create(question=question, text="Projetos")
        Option.objects.create(question=question, text="Redes")
