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

def scrape(request):
    title = request.POST["title"]
    description = request.POST["description"]
    date_created = request.POST["date_created"]

    software = Software(title=title, body=description, datePosted=date_created)
    software.save()

    software = Software.objects.all()
    number = len(software)

    context = {
        'software': software,
        'number': number
    }

    return render(request, 'software/results.html')

def add(request):
    context = {
        'pageinfo': "Add Software",
    }

    return render(request, 'software/edit.html', context)


def edit(request, id):
    software = Software.objects.get(id=id)

    context = {
        'pageinfo': "Edit Software",
        'software': software
    }

    return render(request, 'software/edit.html', context)


def submit(request):
    title = request.POST["title"]
    description = request.POST["description"]
    date_created = request.POST["date_created"]

    software = Software(title=title, body=description, datePosted=date_created)
    software.save()

    software = Software.objects.all()
    number = len(software)

    context = {
        'software': software,
        'number': number
    }

    return render(request, 'software/results.html', context)
