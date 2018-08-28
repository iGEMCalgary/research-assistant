from django.contrib import admin

# Register your models here.
from .models import Protocol, Step

admin.site.register(Protocol)
admin.site.register(Step)