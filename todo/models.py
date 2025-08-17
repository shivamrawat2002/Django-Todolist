from email.policy import default
from django.db import models

# Create your models here.
class Todo(models.Model): #todo is the name of table
    title = models.CharField(max_length=300)
    description = models.TextField()
    completed = models.BooleanField(default=False)

