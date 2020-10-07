from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    url(r'^archive', views.archive, name='archive')
]