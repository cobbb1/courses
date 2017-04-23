__author__ = 'Administrator'

from django.conf.urls import url

from getlist import getlist,calculateDifficulty,search

urlpatterns=[
    url(r'^search$', search),
    url(r'^rundiff$', calculateDifficulty),
    url(r'^(?P<chapter_id>.+)' , getlist)
]