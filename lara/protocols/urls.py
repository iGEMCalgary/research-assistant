from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.results, name='results'),
    url(r'^add_protocol', views.add, name='add'),
    url(r'^submit_protocol', views.submit, name='submit'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')
]
