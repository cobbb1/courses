__author__ = 'Administrator'





from mathematics.models import Useful,Users,Question
from mathematics.server.getresponse import get_response
from django.views.decorators.csrf import csrf_exempt

import datetime
import re

@csrf_exempt
def usefulquestions(request,questionid,userid):
    if request.GET.has_key("choice")==0:
        return get_response(403,"",{})
    e = Users.objects.filter(id=userid)
    if e.count()==0:
        return get_response(403,"",{})
    z = Question.objects.filter(id=questionid)
    if z.count()==0:
        return get_response(403,"",{})
    o = Useful.objects.filter(questionid=questionid,userid=userid)
    if o.count()!=0:
        return get_response(200,"",{})
    o = Useful(questionid=z[0],userid=e[0],answer=int(request.GET["choice"]),time=datetime.datetime.now(),right=1)
    o.save()
    return get_response(200,"",{})
