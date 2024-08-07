from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from .views import ListDetail, ToDoList, ListUpdate, ListCreate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('task/', TaskList.as_view(), name="task"),
    #path('todo-list/<int:pk>/', ListDetail.as_view(), name="todo_list"),
    #path('', ListDetail.as_view(), name="todo_list"),
    path('', ToDoList.as_view(), name="todo"),
    #path('todo_list/<int:pk>/', ListDetail.as_view(), name="list-detail"),

    path('todo_list/', TaskList.as_view(), name="list-detail"),

    path('list-update/<int:pk>/', ListUpdate.as_view(), name="list-update"),
    path('list-create/', ListCreate.as_view(), name="list-create"),
    



    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="tasks-detail"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="tasks-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="tasks-delete")
]