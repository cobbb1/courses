__author__ = 'Administrator'


from django.core import serializers
from django.http import HttpResponse
from mathematics.models import Connect,Neuron,UserQuestion,Question

from django.db.models import F

import json


def getlist(request,chapter_id):
    neurons = Neuron.objects.filter(chapter=chapter_id).values()
    neurone = []
    for neuron in neurons:
        example = list(Question.objects.filter(linkneuron=neuron["id"]).filter(category=1).values_list("id",flat=True))
        exercise = list(Question.objects.filter(linkneuron=neuron["id"]).filter(category=2).values_list("id",flat=True))
        neuron["exercise"]=exercise
        neuron["example"]=example
    neurons = list(neurons)
    return HttpResponse(json.dumps(neurons),content_type="applcation/text")

def calculateDifficulty(request):
    frontweight = 1.0;
    latterweight = 1.5;
    threshold = 10.0;
    neurons = Neuron.objects.all()
    questions = Question.objects.all()
    userquestions = UserQuestion.objects.all()
    # recalculate each question's difficulty
    for neuron in neurons:
        records = userquestions.filter(questionid__in = Question.objects.filter(linkneuron = neuron))
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
        neuron.calculateddifficulty = difficulty
    return HttpResponse(
        serializers.serialize("json", neurons, fields=("title", "calculateddifficulty")),
        content_type="application/json")

def search(request):
    if request.GET.has_key('keyword'):
        keyword = request.GET["keyword"]
        result = Neuron.objects.filter(title__icontains=keyword)
        return HttpResponse(serializers.serialize("json", result), content_type="application/json")