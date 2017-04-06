__author__ = 'Administrator'





from django.core.serializers import serialize
from mathematics.server.getresponse import get_response
from mathematics.models import Question

def get(request,id):
    z = Question.objects.filter(id=id).defer("answer")
    if z.count()==1:
        return get_response(200,serialize("json",z[0]),{})
    else:
        return get_response(200,'{"e":"no"}',{})