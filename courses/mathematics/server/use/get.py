__author__ = 'Administrator'




from django.http import HttpResponseRedirect
from mathematics.server.getresponse import get_response
from mathematics.models import Users


from mathematics.server.action.create import create
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get(request,token):
    z = Users.objects.filter(token=token)
    if z.count()==0:
        return get_response(200,'{"message":"you are not the people in the program"}',{})
    else:
        o = HttpResponseRedirect("http://lala.ust.hk:8000")
        o.set_cookie("token",token)
        o.set_cookie("id",z[0].pk)
        o.set_cookie("userid",z[0].names)
        create(request,o,z[0].pk)
        return o


