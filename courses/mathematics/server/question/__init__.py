__author__ = 'Administrator'



from mathematics.server.getresponse import get_response
from mathematics.models import Question
from django.core.serializers import serialize


def get(request,id):
    e = Question.objects.filter(id=id)
    if e.count()==1:
        return get_response(200,serialize(e[0]),{})
    else:
        return get_response(200,"no",{})