__author__ = 'Administrator'





from django.core.serializers import serialize
from mathematics.server.getresponse import get_response
from mathematics.models import Question

def get(request,id):
    z = Question.objects.filter(id=id).defer("answer")
    if z.count()==1:
        w = [m.name for m in Question._meta.get_fields()]
        w.remove("answer")
        w.remove("linkneuron")
        w.remove("rightproblems")
        w.remove("wrongproblems")
        w.remove("twinproblems")
        w.remove("users")
        w.remove("userquestion")
        return get_response(200,serialize("json",z,fields=tuple(w)),{})
    else:
        return get_response(200,'{"e":"no"}',{})