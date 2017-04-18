__author__ = 'Administrator'

from django.conf.urls import url

from getlist import getlist

urlpatterns=[
    url(r'^(?P<chapter_id>.+)' , getlist)
]