from django.db import models
from datetime import datetime

# Create your models here.


class Notebook(models.Model):
    title = models.CharField(max_length=200)
    datePosted = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Note(models.Model):
    body = models.TextField()
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)
