__author__ = 'Administrator'





from django.core.serializers import serialize
from django.http import HttpResponse
from mathematics.server.getresponse import get_response
from mathematics.models import UserQuestion,Question,Users
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from neuron import neuron

@csrf_exempt
def atquestion(request,userid,questionid):
    userid=int(userid)
    questionid=int(questionid)
    print(questionid)
    if request.POST.has_key("choice")==0:
        return get_response(403,'{"message":"no choice"}',{})
    p = Question.objects.filter(id=questionid)
    if p.count()==0:
        return get_response(403,'{"message":"no question"}',{})
    e = Users.objects.filter(id=userid)
    if e.count()==0:
        return get_response(403,'{"message":"no use"}',{})
    userid = Users.objects.filter(id=userid)[0]
    questionid = Question.objects.filter(id=questionid)[0]
    if request.POST["choice"]==p[0].answer:
        l = "right"
    else:
        l = "wrong"

    e = UserQuestion.objects.filter(questionid=questionid,userid=userid,righte=0)
    if e.count()==0:
        z = UserQuestion(righte=1,questionid=questionid,userid=userid,answer=request.POST["choice"],time=datetime.now(),right=p[0].answer,correct=l)
        z.save()


    if p[0].answer==request.POST["choice"]:
        e = neuron(userid,questionid)
        return get_response(200,'{"message":"right"}',{})
    else:
        w = neuron(userid,questionid)
        return get_response(200,'{"message":"wrong"}',{})

