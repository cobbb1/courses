__author__ = 'Administrator'




from django.conf.urls import url
from get import get
from getlist import getlist

urlpatterns = [
    url(r'^/(?P<id>.+?)' , get),
    url(r'^' , getlist)
]