__author__ = 'Administrator'






from django.conf.urls import url

from evaluate import evaluate



urlpatterns=[
    url(r'^(?P<userid>.+)',evaluate)
]