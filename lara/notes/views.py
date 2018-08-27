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
