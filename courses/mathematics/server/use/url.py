__author__ = 'Administrator'



from django.conf.urls import url
from get import get

urlpatterns = [
    url(r'^(?P<token>.+?)$' , get)
]