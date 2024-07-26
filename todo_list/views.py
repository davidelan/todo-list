from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Todo_list, Task

# Create your views here.

class TaskList(ListView):
    model = Task

    # context_object_name = 'task'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['task'] = context['task'].filter(user=self.request.user)
    #     context['count'] = context['task'].filter(complete=False).count()

    #     search_input = self.request.GET.get('search-area') or ''
    #     if search_input:
    #         context['task'] = context['task'].filter(title__icontains = search_input)
    #         context['search_input'] = search_input
    #     return context