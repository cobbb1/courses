__author__ = 'Administrator'





from django.core.serializers import serialize
from mathematics.models import Question,Neuron
from mathematics.server.getresponse import get_response


def getlist(request):
    w = Question.objects.only("id","category","code","difficulty","sensitivity")
    print(w)
    if request.GET.has_key("neurons"):
        w = Neuron.objects.filter(id=int(request.GET["neurons"]))[0].question_set.only("question__code","question__category","question__id")
    if request.GET.has_key("difficulty"):
        w = w.filter(difficulty=int(request.GET["difficulty"]))
    return get_response(200,serialize("json",w),{})