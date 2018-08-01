from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.software, name='software'),
    url(r'^add_software', views.addSoftware, name='addSoftware'),
    url(r'^submit_software', views.submitSoftware, name='submitSoftware'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')
]
