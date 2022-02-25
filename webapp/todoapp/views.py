from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateTodoForm
from .models import Todo

def home(request):
    all_todos = Todo.objects.all().order_by('due_date')
    context = {'all_todos': all_todos}
    return render(request, 'todoapp/home.html', context)

def create_todo(request):
    form = CreateTodoForm()

    if request.method == 'POST':
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todoapp')

    context = {'form':form}

    return render(request, 'todoapp/create_todo.html', context)
