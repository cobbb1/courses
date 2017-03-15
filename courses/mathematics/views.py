from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    # mytemplate = loader.get_template('myserver/testMarkdown.html')
    # return HttpResponse(mytemplate)
    # why the above do not work??????
    return render(request, 'mathematics/testMarkdown.html',None)

import json
from django.core import serializers
from .models import Question
def get(request,code):
    response_data = {}
    # response_data['test'] = "# Marked in browser\n\nRendered by **marked**. $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$"
    response_data= Question.objects.filter(code=code)
    print(response_data)
    print("*********************")
    return HttpResponse(serializers.serialize("json",response_data), content_type="application/json")
   # return "# Marked in browser\n\nRendered by **marked**. $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$"

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