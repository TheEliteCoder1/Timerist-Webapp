from django.urls import path

from . import views

urlpatterns = [
    # /todoapp -> base_url + /todoapp
    path('', views.home, name='home'),
    path('create_todo', views.create_todo, name='create_todo'),
    # /todoapp/...etc -> base_url + /todoapp + etc...
    # path('<int:todo_id>/', views.edit, name='edit'), // edit todo
]