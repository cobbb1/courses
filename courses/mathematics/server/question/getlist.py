__author__ = 'Administrator'

from django.core.serializers import serialize
from mathematics.models import Question,Neuron
from mathematics.server.getresponse import get_response
from django.http import HttpResponse
from django.core import serializers
import json

def getlist(request):
    w = Question.objects.only("id","category","code","difficulty","sensitivity")
    if request.GET.has_key("neurons"):
        w = Question.objects.filter(linkneuron=Neuron.objects.filter(id=int(request.GET["neurons"]))[0]).only("id", "category", "code", "difficulty", "sensitivity")
        print(w)
    if request.GET.has_key("difficulty"):
        w = w.filter(difficulty=int(request.GET["difficulty"]))
        print(w)
    return HttpResponse(serializers.serialize("json", w, fields=("id","category","code","difficulty","sensitivity")), content_type="application/json")