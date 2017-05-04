__author__ = 'Administrator'




from django.conf.urls import url
from get import get
from getlist import getlist,calculateDifficulty,getmostdone,getmostdifficulty,getmostuseful,search,getcount,getquestionbychapter,get2weekmostdone

urlpatterns = [
    url(r'^getbychapter', getquestionbychapter),
    url(r'^search', search),
    url(r'^mostdiff', getmostdifficulty), # according to accuracy
    url(r'^mostuseful', getmostuseful),
    url(r'^mostdone', getmostdone),
    url(r'^2weekmostdone', get2weekmostdone),
    url(r'^rundiff', calculateDifficulty),
    url(r'^getcount',getcount),
    url(r'^(?P<id>.+)' , get),
    url(r'^' , getlist)
]