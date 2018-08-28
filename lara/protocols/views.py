from django.shortcuts import render

from .models import Protocol, Step

# Create your views here.


def results(request):
    protocols = Protocol.objects.all()
    number = len(protocols)

    context = {
        'protocols': protocols,
        'number': number
    }

    return render(request, 'protocols/results.html', context)


def details(request, id):
    protocol = Protocol.objects.get(id=id)
    steps = protocol.step_set.all()

    context = {
        'protocol': protocol,
        'steps': steps
    }

    return render(request, 'protocols/details.html', context)

def add(request):
    context = {
        'pageinfo': "Add Protocol",
    }

    return render(request, 'protocols/edit.html', context)

def submit(request):
    title = request.POST["title"]
    steps = request.POST["steps"]
    date_created = request.POST["date_created"]

    protocol = Protocol(title=title, datePosted=date_created)
    protocol.save()

    step = Step(body=steps, protocol=protocol)
    step.save()

    protocols = Protocol.objects.all()
    number = len(protocols)

    context = {
        'protocols': protocols,
        'number': number
    }

    return render(request, 'protocols/results.html', context)
