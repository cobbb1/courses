__author__ = 'Administrator'


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$' , views.index, name="zc"),
    url(r'^(?P<code>.+)$', views.get, name='index'),
]