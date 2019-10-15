from django.forms.formsets import formset_factory
from django.forms import ModelForm, inlineformset_factory

from .models import Question, Choice

class ChoiceForm(ModelForm):
    class Meta:
        fields = ('choice_text',)
        model = Choice


class QuestionForm(ModelForm):
    class Meta:
        fields = ('question_text',)
        model = Question




ChoiceFormSet = formset_factory(ChoiceForm, extra=0, min_num=3, validate_min=True)
