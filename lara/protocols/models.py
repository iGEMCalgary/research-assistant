from django.db import models
from datetime import datetime

# Create your models here.


class Protocol(models.Model):
    title = models.CharField(max_length=200)
    datePosted = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Step(models.Model):
    body = models.TextField()
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE)
