from django import forms
from .models import *

class CommentForm(forms.Form):
    text = forms.CharField(label='текст:', max_length=200)
    author = forms.CharField(label='аффтар:', max_length=20)

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class DirectorModelForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'