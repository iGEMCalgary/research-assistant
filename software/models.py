from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
import datetime

# Create your models here.


class Software(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    link = models.URLField(max_length=200)
    iGemTeamName = models.CharField(max_length=200, blank=True)
    iGemYear = models.CharField(max_length=4, blank=True)
    dateSubmitted = models.DateField(default=datetime.date.today)
    dateModified = models.DateField(default=datetime.date.today)

    def get_absolute_url(self):
        return reverse('software:details', kwargs={'pk': self.pk})

    # title = models.CharField(max_length=200)
    # description = RichTextField()
    # link = models.CharField(max_length=200)
    # iGemTeamName = models.CharField(max_length=200, blank=True)
    # iGemYear = models.CharField(max_length=4, blank=True)
    # dateSubmitted = models.DateField(default=datetime.date.today)
    # dateModified = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Software"
