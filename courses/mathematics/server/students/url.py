__author__ = 'Administrator'

from django.conf.urls import url
from getsortedlist import getSortedStudentList,getDoneRecord

urlpatterns = [
    url(r'^donerecord', getDoneRecord),
    url(r'^sort' , getSortedStudentList)
]