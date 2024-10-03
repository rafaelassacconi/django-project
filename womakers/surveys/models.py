# Docs
# - Model example: https://docs.djangoproject.com/en/5.1/topics/db/models/#quick-example
# - Fields: https://docs.djangoproject.com/en/5.1/ref/models/fields/
# - DateField: https://docs.djangoproject.com/en/5.1/ref/models/fields/#datefield

from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.text

class Option(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class Vote(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.option.text
