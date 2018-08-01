from django.db import models
from datetime import datetime

# Create your models here.
class Software(models.Model):
    team = models.CharField(max_length=200)
    body = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.team
    class Meta:
        verbose_name_plural = "Software"