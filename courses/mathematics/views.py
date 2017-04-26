from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    # mytemplate = loader.get_template('myserver/testMarkdown.html')
    # return HttpResponse(mytemplate)
    # why the above do not work??????
    return render(request, 'mathematics/testMarkdown.html',None)


def indexw(request):
    # mytemplate = loader.get_template('myserver/testMarkdown.html')
    # return HttpResponse(mytemplate)
    # why the above do not work??????
    return render(request, 'mathematics/index.html',None)

def indexz(request):
    # mytemplate = loader.get_template('myserver/testMarkdown.html')
    # return HttpResponse(mytemplate)
    # why the above do not work??????
    return render(request, 'mathematics/neuron.html',None)

import json
from django.core import serializers
from .models import Question,Neuron




def get(request,code):
    response_data = {}
    # response_data['test'] = "# Marked in browser\n\nRendered by **marked**. $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$"
    # response_data= list(Question.objects.filter(code=code).values())
    response_data = Question.objects.filter(code=code)
    response_data = list(response_data.values())
    # return HttpResponse(serializers.serialize("json",response_data), content_type="application/json")
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getneuron(request):
    print("===================")
    ti = request.GET.get('title')
    print("--------------------")
    print(type(ti))
    response_data= list(Neuron.objects.filter(title=ti).values())
    #print(response_data)
    #print(serializers.serialize("json",response_data))
    # return HttpResponse(serializers.serialize("json",response_data), content_type="application/json")
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def preview(request):
    print("===================")
    typ = request.GET.get('type')
    code = request.GET.get('code')
    print("--------------------")
    print(type(code))
    print(type(typ))
    response_data= list(Question.objects.filter(code=code,category=typ).values())
    #print(response_data)
    #print(serializers.serialize("json",response_data))
    # return HttpResponse(serializers.serialize("json",response_data), content_type="application/json")
    return HttpResponse(json.dumps(response_data), content_type="application/json")

import datetime
def allquestion(request):
    response_data = Question.objects.all()
    if request.GET.has_key("category"):
        response_data = response_data.filter(category=int(request.GET["category"]))
    response_data = list(response_data.values())
    # return HttpResponse(serializers.serialize("json", response_data), content_type="application/json")
    return HttpResponse(json.dumps(response_data), content_type="application/json")
