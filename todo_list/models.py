from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Todo_list(models.Model):
    """
    A model representing a TO-DO List.

    Attributes:
        list_id (SlugField): Unique slug identifier
        title (CharField): Unique identifier for the todo_list.
        user (ForeignKey): User who created the todo_list.
    """
    list_id = models.SlugField(max_length=200, unique=True, null=True)
    title = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="todo_lists"
    )

    def get_absolute_url(self):
        return reverse("list", args=[self.id])
   
    def __str__(self):
        return self.title


class Task(models.Model):
    """
    A model representing a Task in the TO-DO list.

    Attributes:
        user (ForeignKey): User who created the task.
        todo_list (ForeignKey): relation to Todo_list model
        title (CharField): Unique identifier for the task.
        description (TextField): Description of the task.
        created_on (DateTimeField): Timestamp when the task was created.
        updated_on (DateTimeField): Timestamp when the task was last
        updated.
    """
    title = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_items", null=True, blank=True)
    todo_list = models.ForeignKey(Todo_list, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse(
            "tasks-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return self.title
        #return f"{self.title} | crated {self.created_on}"
       
        
    class Meta:
        ordering = ['created_on']


    

