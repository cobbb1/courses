from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    # mytemplate = loader.get_template('myserver/testMarkdown.html')
    # return HttpResponse(mytemplate)
    # why the above do not work??????
    return render(request, 'mathematics/testMarkdown.html',None)

from django.views.decorators.cache import cache_control
@cache_control(max_age=3600)
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
    # response_data['test'] = "# Marked in browser\n\nRendered by **marked**. $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$"
    # response_data= list(Question.objects.filter(code=code).values())
    response_data = Question.objects.filter(code=code)
    return HttpResponse(serializers.serialize("json",response_data), content_type="application/json")
    # return HttpResponse(json.dumps(response_data), content_type="application/json")

def getneuron(request):
    print("===================")
    ti = request.GET.get('title')
    print("--------------------")
    print(type(ti))
    response_data= Neuron.objects.filter(title=ti)
    #print(response_data)
    #print(serializers.serialize("json",response_data))
    return HttpResponse(serializers.serialize("json",response_data), content_type="application/json")
    # return HttpResponse(json.dumps(response_data), content_type="application/json")


def preview(request):
    print("===================")
    typ = request.GET.get('type')
    code = request.GET.get('code')
    print("--------------------")
    print(type(code))
    print(type(typ))
    response_data= Question.objects.filter(code=code,category=typ)
    #print(response_data)
    #print(serializers.serialize("json",response_data))
    return HttpResponse(serializers.serialize("json",response_data), content_type="application/json")
    # return HttpResponse(json.dumps(response_data), content_type="application/json")

def allquestion(request):
    response_data = Question.objects.all()
    if request.GET.has_key("category"):
        response_data = response_data.filter(category=int(request.GET["category"]))
    if request.GET.has_key("difficulty"):
        response_data = response_data.filter(difficulty=int(request.GET["difficulty"]))
    response_data2 = list(response_data.values())
    result_list = []
    for item in response_data2:
        questionid = item["id"]
        this = response_data.filter(id = questionid)[0]

        linkneuron = list(this.linkneuron.values("title","chapter"))
        # linkneuron = [e["id"] for e in linkneuron]
        #print(linkneuron)
        rightproblems = this.rightproblems.values("id")
        rightproblems = [e["id"] for e in rightproblems]
        # print(rightproblems)
        wrongproblems = this.wrongproblems.values("id")
        wrongproblems = [e["id"] for e in wrongproblems]
        # print(wrongproblems)
        twinproblems = this.wrongproblems.values("id")
        twinproblems = [e["id"] for e in twinproblems]   # print(twinproblems)

        item["linkneuron"]=linkneuron
        item["rightproblems"]=rightproblems
        item["wrongproblems"]=wrongproblems
        item["twinproblems"]=twinproblems

        codes = str(item["code"]).split(".")
        chaptercode = codes[0]
        subchaptercode = codes[1]
        problemcode = 0
        if len(codes) > 2:
            problemcode = int(codes[2])


        item["chaptercode"] = int(chaptercode)
        item["subchaptercode"] = int(subchaptercode)
        item["problemcode"] = int(problemcode)
        result_item={"pk":questionid,"fields":item}
        result_list.append(result_item)

    result_list = sorted(result_list, key=lambda temp: (temp['fields']['chaptercode'],temp['fields']['subchaptercode'],temp['fields']['problemcode']))
    # return HttpResponse(serializers.serialize("json", response_data), content_type="application/json")
    # return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps(result_list), content_type="application/json")
