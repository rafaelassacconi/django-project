# Docs
# - Form example: https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-editing/#model-forms
# - ModelChoiceField: https://docs.djangoproject.com/en/5.1/ref/forms/fields/#django.forms.ModelChoiceField
# - RadioSelect: https://docs.djangoproject.com/en/5.1/ref/forms/widgets/#radioselect
# - Form init example: https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/#changing-the-queryset

from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    option = forms.ModelChoiceField(empty_label="", 
                                    label="Selecione uma opção:", 
                                    required=True, 
                                    queryset=None, 
                                    widget=forms.RadioSelect)

    class Meta:
        model = Question
        fields = ["option"]

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)
        super().__init__(*args, **kwargs)
        self.fields['option'].queryset = question.option_set.all()
