from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^software/$', views.SoftwareList.as_view(), name='list'),
    url(r'^software/details/(?P<pk>\d+)/$', views.SoftwareDetails.as_view(), name='details'),
    url(r'^software/add/$', views.SoftwareCreate.as_view(), name='create'),
    url(r'^software/details/(?P<pk>\d+)/update/$', views.SoftwareUpdate.as_view(), name='update'),
    url(r'^software/details/(?P<pk>\d+)/delete/$', views.SoftwareDelete.as_view(), name='delete'),
    # url(r'^software/scrape/$', views.scrape , name='scrape'),
]
