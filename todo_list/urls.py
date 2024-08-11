from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate
from .views import TaskDelete, CustomLoginView, RegisterPage


urlpatterns = [
    path('', TaskList.as_view(), name="task"),  # Landing page

    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="tasks-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="tasks-delete")
]