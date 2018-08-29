from django.contrib import admin

# Register your models here.
from .models import Software, Link

admin.site.register(Software)
admin.site.register(Link)
