from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    # mytemplate = loader.get_template('myserver/testMarkdown.html')
    # return HttpResponse(mytemplate)
    # why the above do not work??????
    return render(request, 'myserver/testMarkdown.html',None)

import json
from .models import Question
def get(request,code):
    response_data = {}
    # response_data['test'] = "# Marked in browser\n\nRendered by **marked**. $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$"
    response_data['test'] = Question.objects.get(code=code).problem
    print(response_data['test'])
    return HttpResponse(json.dumps(response_data), content_type="application/json")
   # return "# Marked in browser\n\nRendered by **marked**. $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$"
