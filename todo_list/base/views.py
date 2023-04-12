from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

# from django.contrib.auth.mixins import OwnObjectsMixin

from .models import Task
# Create your views here.

class OwnObjectsMixin():
 """
 Only returns objects that belongs to the current user. Assumes the object
 has a 'user' foreignkey to a User.
 """
 def get_queryset(self):
    user = self.request.user
    return super(OwnObjectsMixin, self).get_queryset().filter(user=user)

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True	
    
    def get_success_url(self):
        return reverse_lazy('tasks')
        


class TaskList(OwnObjectsMixin, ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetails(OwnObjectsMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    
class TaskCreate(OwnObjectsMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskUpdate(OwnObjectsMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    

class TaskDelete(OwnObjectsMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    
