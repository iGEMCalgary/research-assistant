from django.shortcuts import render
from django.http import HttpResponse

from .models import Software

# Create your views here.
def index(request):
    # return HttpResponse("HELLO FROM SOFTWARE")

    software = Software.objects.all()[:10]

    context = {
        'title': 'Software',
        'software': software
    }

    return render(request, 'software/index.html', context)

def details(request, id):
    software = Software.objects.get(id=id)

    context = {
        'software': software
    }

    return render(request, 'software/details.html', context)