__author__ = 'Administrator'



from django.conf.urls import url
from get import get
from getNeuron import getNeuron
from getquestion import getquestion
from atquestion import atquestion
from mathematics.server.action.getuseraction import getuseraction
from usefulquestion import usefulquestions
from preferquestion import preferquestions
from hardnessquestion import hardnequestions

urlpatterns = [
    url(r'^(?P<userid>.+?)/actions',getuseraction),
    url(r'^(?P<userid>.+?)/questions/(?P<questionid>.+?)/prefer',preferquestions),
    url(r'^(?P<userid>.+?)/questions/(?P<questionid>.+?)/hardness',hardnequestions),
    url(r'^(?P<user_id>.+?)/neurons/(?P<chapter_id>.+)' , getNeuron),
    url(r'^(?P<userid>.+?)/questions/(?P<questionid>.+?)/useful',usefulquestions),
    url(r'^(?P<userid>.+?)/questions/(?P<questionid>.+)' , atquestion),
    url(r'^(?P<userid>.+?)/questions/' , getquestion),


    url(r'^(?P<token>.+?)$' , get),

]