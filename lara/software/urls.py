from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.results, name='results'),
    url(r'^add_software', views.add, name='add'),
    url(r'^edit_software/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^submit_software', views.submit, name='submit'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')
]
