from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(
        max_length=120
    )
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title} is completed?: {self.completed}'