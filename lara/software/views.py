from django.shortcuts import render

from .models import Software

# Create your views here.


def results(request):
    software = Software.objects.all()
    number = len(software)

    context = {
        'software': software,
        'number': number
    }

    return render(request, 'software/results.html', context)


def details(request, id):
    software = Software.objects.get(id=id)

    context = {
        'software': software
    }

    return render(request, 'software/details.html', context)


def addSoftware(request):
    return render(request, 'software/addSoftware.html')


def submitSoftware(request):
    title = request.POST["title"]
    description = request.POST["description"]
    date_created = request.POST["date_created"]

    software = Software(team=title, body=description, date_posted=date_created)
    software.save()

    software = Software.objects.all()[:10]

    context = {
        'title': 'Software',
        'software': software
    }

    return render(request, 'software/software.html', context)
