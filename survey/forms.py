from django import forms
from .models import Response, Option

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['question', 'option']
        widgets = {
            'question': forms.HiddenInput(),
        }
