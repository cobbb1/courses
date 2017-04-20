__author__ = 'Administrator'

from django.core.serializers import serialize
from mathematics.models import Question,Neuron,UserQuestion
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

def calculateDifficulty(request):
    frontweight = 1.0;
    latterweight = 1.5;
    threshold = 10.0;
    questions = Question.objects.all()
    userquestions = UserQuestion.objects.all()
    # recalculate each question's difficulty
    for question in questions:
        records = userquestions.filter(questionid = question.id)
        count = 0;
        difficulty = 0.0
        totalweight = 0.0
        for record in records:
            count += 1
            if count <= threshold:
                weight = frontweight
            else:
                weight = latterweight

            if record.correct == 'right':
                difficulty -= weight;
            else:
                difficulty += weight

            totalweight += weight
        if totalweight == 0:
            difficulty = 0.0
        else:
            difficulty /= totalweight
        question.calculateddifficulty = difficulty
    return HttpResponse(
        serializers.serialize("json", questions, fields=("id", "code", "difficulty", "calculateddifficulty")),
        content_type="application/json")