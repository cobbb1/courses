__author__ = 'Administrator'

from django.conf.urls import url
from getsortedlist import getSortedStudentList

urlpatterns = [
    url(r'^sort$' , getSortedStudentList)
]