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
    frontweight = 1.0
    latterweight = 1.5
    threshold = 10.0
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

from django.db.models import Count, Min, Sum, Avg
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

def getmostdone(request):
    userquestions = UserQuestion.objects.all()
    # group by questionid and count number of questions have the same questionid
    questionfrequency = userquestions.values('questionid').annotate(question_count=Count('questionid'))

    #conver it to list, or will not be serialized
    result_list = list(questionfrequency.values('questionid', 'question_count'))
    sorted(result_list, key=lambda temp: temp['question_count'])
    return HttpResponse(json.dumps(result_list))

def getmostuseful(request):
    return

def getmostdifficulty(request):
    userquestions = UserQuestion.objects.all().values("questionid").annotate(Count("questionid"))
    total = 0;
    right = 0;
    lowest_accuracy = 1.0
    lowest_accuracy_id = userquestions[0]["questionid"]
    lowest_accuracy_total = total
    lowest_accuracy_right = 0
    for question in userquestions:
        total = question["questionid__count"]
        right = UserQuestion.objects.filter(questionid = question["questionid"], correct="right").count()
        if total != 0:
            temp_accuracy = float(right) / float(total)
            if temp_accuracy < lowest_accuracy: # most wrong
                lowest_accuracy = temp_accuracy
                lowest_accuracy_id = question["questionid"]
                lowest_accuracy_total = total
                lowest_accuracy_right = right
    record = {"questionid": lowest_accuracy_id, "accuracy": lowest_accuracy, "total":lowest_accuracy_total, "right":lowest_accuracy_right}
    return HttpResponse(json.dumps(record), content_type="application/json")