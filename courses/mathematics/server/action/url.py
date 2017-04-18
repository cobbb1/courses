__author__ = 'Administrator'






from django.conf.urls import url
from getlist import getlist

urlpattern=[
    url(r'^$',getlist)
]