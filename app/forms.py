from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}

class QuetionsForm(forms.ModelForm):
    class Meta:
        model=Quetions
        fields=['quetion']

class AnswersForm(forms.ModelForm):
    class Meta:
        model=Answers
        fields=['quetion','answer']
