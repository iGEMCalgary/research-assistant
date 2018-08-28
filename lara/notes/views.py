from django.shortcuts import render

from .models import Notebook, Note

# Create your views here.


def results(request):
    notebooks = Notebook.objects.all()
    number = len(notebooks)

    context = {
        'notebooks': notebooks,
        'number': number
    }

    return render(request, 'notes/results.html', context)


def details(request, id):
    notebook = Notebook.objects.get(id=id)
    notes = notebook.note_set.all()

    context = {
        'notebook': notebook,
        'notes': notes
    }

    return render(request, 'notes/details.html', context)

def add(request):
    context = {
        'pageinfo': "Add Notes",
    }

    return render(request, 'notes/edit.html', context)

def submit(request):
    title = request.POST["title"]
    notes = request.POST["notes"]
    date_created = request.POST["date_created"]

    notebook = Notebook(title=title, datePosted=date_created)
    notebook.save()

    note = Note(body=notes, notebook=notebook)
    note.save()

    notebooks = Notebook.objects.all()
    number = len(notebooks)

    context = {
        'notebooks': notebooks,
        'number': number
    }

    return render(request, 'notes/results.html', context)
