__author__ = 'Administrator'






from django.db.models import Max,Min
from django.db.models import F
from mathematics.models import Action
from mathematics.server.getresponse import get_response
from django.core.serializers.json import DjangoJSONEncoder
import json



def getuseraction(request,userid):
    e = Action.objects.filter(userid=userid)
    z = e.values("token").annotate(log=Max("time"),out=Min("time"))
    return get_response(200,json.dumps(list(z),cls=DjangoJSONEncoder),{})