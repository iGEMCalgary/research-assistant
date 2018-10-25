from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Software

from .runScrape2 import main
import datetime

# Create your views here.


def home(request):
    return render(request, 'software/home.html')

def search(request):
    query = request.GET.get('q')
    if query:
        software = software.filter(
            Q(title=query) |
            Q(description=query) |
            Q(iGemTeamName=query) |
            Q(iGemYear=query)
        )
    context = {
        'software_list': software
    }
    print("HELLO")

    return render(request, 'software/list.html', context)


class SoftwareList(generic.ListView):
    template_name = 'software/list.html'
    context_object_name = 'software_list'

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'dateSubmitted')
        return Software.objects.all().order_by(order)
        # return Software.objects.all().order_by('dateSubmitted')

    def get_context_data(self, **kwargs):
        teams = []
        descriptions = []
        if(self.request.GET.get('mybtn')):
            print("IN GET_CONTEXT_DATA")
            year = int(self.request.GET.get('mytextbox'))
            main(year, teams, descriptions)
            for i in range(len(teams)):
                link = "http://" + str(year) + ".igem.org/Team:" + teams[i]
                software = Software(title=teams[i], description=descriptions[i], link=link, iGemTeamName=teams[i], iGemYear=str(year), dateSubmitted=datetime.datetime.today(), dateModified=datetime.datetime.today())
                software.save()
        
        if(self.request.GET.get('q')):
            query = self.request.GET.get('q')
            software = Software.objects.all()
            software = software.filter(
                Q(title=query) |
                Q(description=query) |
                Q(iGemTeamName=query) |
                Q(iGemYear=query)
            )
            context = {
                'software_list': software
            }
            return context

        context = super(SoftwareList, self).get_context_data(**kwargs)
        context['orderby'] = self.request.GET.get('orderby')
        return context


class SoftwareDetails(generic.DetailView):
    model = Software
    template_name = 'software/details.html'


class SoftwareCreate(generic.CreateView):
    model = Software
    fields = ['title', 'description', 'link', 'iGemTeamName', 'iGemYear', 'dateSubmitted', 'dateModified']


class SoftwareUpdate(generic.UpdateView):
    model = Software
    fields = ['title', 'description', 'link', 'iGemTeamName', 'iGemYear', 'dateSubmitted', 'dateModified']


class SoftwareDelete(generic.DeleteView):
    model = Software
    success_url = reverse_lazy('software:list')
