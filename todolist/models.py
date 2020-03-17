from django.db import models

# Create your models here.
class TodoItem(models.Model):

    def __str__(self):
        return self.field

    field = models.TextField()
