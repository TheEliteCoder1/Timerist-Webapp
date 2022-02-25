from attr import attrs
from django import forms
from django.forms import ModelForm
from .models import *


class CreateTodoForm(forms.ModelForm):
	task=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write the name of your task...', 'class':'form-control'}))
	description=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Describe it a little more...', 'class':'form-control', 'id':'exampleFormControlTextarea1', 'rows':3}))
	due_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'format':'yyyy-MM-dd'}))
	class Meta:
		model = Todo
		fields = ['task', 'description', 'due_date']