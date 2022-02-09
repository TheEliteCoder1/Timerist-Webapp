from django import forms
from django.forms import ModelForm
from .models import *


class CreateTodoForm(forms.ModelForm):
	task=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
	class Meta:
		model = Todo
		fields = ['task', 'description', 'due_date']