# Core
from django.conf.urls import url
from cos_site import views


urlpatterns = [
    url(r'^$', views.index, name='site_index'),
]
