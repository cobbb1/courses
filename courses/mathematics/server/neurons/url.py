__author__ = 'Administrator'

from django.conf.urls import url

from getlist import getlist,calculateDifficulty

urlpatterns=[
    url(r'^rundiff', calculateDifficulty),
    url(r'^(?P<chapter_id>.+)' , getlist)
]