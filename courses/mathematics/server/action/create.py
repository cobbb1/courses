__author__ = 'Administrator'





from django.views.decorators.csrf import csrf_exempt
from mathematics.models import Action,Users



from datetime import datetime


@csrf_exempt
def create(request,response,userid):
    w = datetime.now()
    if request.method=="GET":
        z = request.GET
    if request.method=="POST":
        z = request.POST
    if request.COOKIES.has_key("token")==0:
        print("2")
        return 0
    userid = Users.objects.filter(id=userid)
    if userid.count()!=1:
        print("1")
        return 0
    userid = userid[0]
    action = Action(userid=userid,url=request.path,request=z,time=w,response=response.content,responsestatus=response.status_code,token=request.COOKIES["token"])
    action.save()
    return 1