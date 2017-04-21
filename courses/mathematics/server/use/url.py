__author__ = 'Administrator'



from django.conf.urls import url
from get import get
from getNeuron import getNeuron
from getquestion import getquestion
from atquestion import atquestion
from mathematics.server.action.getuseraction import getuseraction

urlpatterns = [
    url(r'^(?P<userid>.+?)/actions',getuseraction),


    url(r'^(?P<user_id>.+?)/neurons/(?P<chapter_id>.+)' , getNeuron),
    url(r'^(?P<userid>.+?)/questions/(?P<questionid>.+)' , atquestion),
    url(r'^(?P<userid>.+?)/questions/' , getquestion),


    url(r'^(?P<token>.+?)$' , get),

]