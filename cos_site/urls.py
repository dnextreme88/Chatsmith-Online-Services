# Core
from django.conf.urls import url
from cos_site import views


urlpatterns = [
    url(r'^$', views.index, name='site_index'),
    url(r'^dashboard_profile/$', views.dashboard_profile, name='dashboard_profile'),
    url(r'^focal/$', views.focal, name='focal'),
    url(r'^plateiq/$', views.plateiq, name='plateiq'),
    url(r'^persistiq/$', views.persistiq, name='persistiq'),
    url(r'^smartalto/$', views.smart_alto, name='smart_alto'),
    url(r'^knowledgebase/$', views.knowledge_base, name='knowledge_base'),
]
