__author__ = 'Administrator'





from mathematics.models import Prefer,Users,Question
from mathematics.server.getresponse import get_response
from django.views.decorators.csrf import csrf_exempt

import datetime
import re

@csrf_exempt
def preferquestions(request,questionid,userid):
    if request.GET.has_key("choice")==0:
        return get_response(403,"no choice",{})
    e = Users.objects.filter(id=userid)
    if e.count()==0:
        return get_response(403,"no such user",{})
    z = Question.objects.filter(id=questionid)
    if z.count()==0:
        return get_response(403,"no such question",{})
    o = Prefer.objects.filter(questionid=questionid,userid=userid)
    if o.count() == 0:
        # return get_response(200,"",{})
        o = Prefer(questionid=z[0],userid=e[0],answer=int(request.GET["choice"]),time=datetime.datetime.now(),right=1)
        o.save()
        return get_response(200,"success",{})
    else:
        return get_response(500, "failed", {})