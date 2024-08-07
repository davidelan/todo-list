from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task, Todo_list

# Create your views here.

class ToDoList(LoginRequiredMixin, ListView):
    model = Todo_list
    context_object_name = 'todo'

    ### Context data to prevent user to access other users data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo'] = context['todo'].filter(user=self.request.user)

        ### Lists count
        context['count'] = context['todo'].count()

        ### search capability for tasks
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['todo'] = context['todo'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context

    


class ListDetail(LoginRequiredMixin, DetailView):
    model = Todo_list
    context_object_name = 'todo'
    template_name = "todo_list/task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(todo_list=self.object)
        return context

# class ListView(ListView):
#     model = Todo_list
#     template_name = "todo_list/todo_list.html"


# class ListCreate(LoginRequiredMixin, CreateView):
#     model = Todo_list
#     fields = ['title']
#     success_url = reverse_lazy('list')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(ListCreate, self).form_valid(form)

class ListUpdate(LoginRequiredMixin, UpdateView):
    model = Todo_list
    fields = ['title', 'content']
    success_url = reverse_lazy('todo')


class ListCreate(LoginRequiredMixin, CreateView):
    model = Todo_list
    fields = ['title', 'content']
    success_url = reverse_lazy('todo')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListCreate, self).form_valid(form)



######## TASK views

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task'

    ### Context data to prevent user to access other users data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)

        ### Incomplete tasks count
        context['count'] = context['task'].filter(complete=False).count()

        ### search capability for tasks
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['task'] = context['task'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "todo_list/task.html"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task')


class CustomLoginView(LoginView):
    template_name = 'todo_list/login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('todo')


class RegisterPage(FormView):
    template_name = 'todo_list/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    ### in order to go back to task if trying to load register page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(RegisterPage, self).get(*args, *kwargs)