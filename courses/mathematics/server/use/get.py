__author__ = 'Administrator'



from django.core import serializers
from mathematics.server.getresponse import get_response
from mathematics.models import Users

def get(request,token):
    users = Users.objects.filter(token=token)
    if users.count()==0:
        return get_response(403,"{'message':''}",{})
    else:
        z = get_response(200,"{'userid':'%s'}" % users[0].names,{"token":token})
        z.set_default("location","lala.ust.hk:8000")
        return z