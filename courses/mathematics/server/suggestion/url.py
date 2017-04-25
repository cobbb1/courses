__author__ = 'Administrator'
from django.conf.urls import url
from get import getSystemSuggestion,postSystemSuggestion,getQuestionSuggestion,postQuestionSuggestion


urlpatterns = [
    url(r'^system/all', getSystemSuggestion),
    url(r'^system/upload', postSystemSuggestion),
    url(r'^question/all', getQuestionSuggestion),
    url(r'^question/upload' , postQuestionSuggestion)
]