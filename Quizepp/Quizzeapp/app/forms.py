from django import forms
from .models import Quize,question

class quizeForm(forms.ModelForm):
    class Meta:
        model = Quize
        fields =["tittle"]

class questionForm(forms.ModelForm):
    class Meta:
        model=question
        fields=['text','question1','question2','question3','question4','correct']