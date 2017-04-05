__author__ = 'Administrator'



from django.conf.urls import url
from get import get
from getNeuron import getNeuron

urlpatterns = [
    url(r'^(?P<token>.+?)$' , get),
    url(r'^(?P<user_id>.+?)/neurons/(?P<chapter_id>.+?)' , getNeuron)
]