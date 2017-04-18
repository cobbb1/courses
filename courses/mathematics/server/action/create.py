__author__ = 'Administrator'





from django.views.decorators.csrf import csrf_exempt
from mathematics.models import Action,Users
import re



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
    l = ""
    if response.status_code==200 and len(re.findall("/get/api",request.path))!=0:
        l = response.content
    userid = userid[0]
    action = Action(userid=userid,url=request.path,request=z,time=w,response=l,responsestatus=response.status_code,token=request.COOKIES["token"])
    action.save()
    return 1