__author__ = 'Administrator'






from mathematics.models import Action
from mathematics.server.getresponse import get_response
import re


def getlist(request):
    w = Action.objects.all()
    z = w.values()
    e = open("theall/ew.csv","w")
    for l in z[0]:
        e.write(str(l)+",")
    e.write("\n")
    for w in z:
        for p,o in w.items():
            if p!="content":
                e.write(str(o)+",")
            else:
                e.write(pro(w["url"],w["method"])+",")
        e.write("\n")
    e.close()
    return get_response(200,"lala.ust.hk:8000/theall/ew.csv",{})


def pro(w,e):
    print(w)
    if len(re.findall("/get/api/users/.+?/questions/.+",w))!=0 and e=="GET":
        return "usersquestions"
    if len(re.findall("/get/api/users/.+?/questions/.+",w))!=0 and e=="POST":
        return "usersdoingquestions"
    if len(re.findall("/get/api/users/.+?/neurons/.+",w))!=0:
        return "usersneurons"
    if len(re.findall("/get/api/users/.+",w))!=0:
        return "log"
    if len(re.findall("/get/api/neurons/.+",w))!=0:
        return "neurons"
    if len(re.findall("/get/api/connects/.+",w))!=0:
        return "connects"
    if len(re.findall("/get/api/questions/.+",w))!=0:
        return "questionget"
    if len(re.findall("/get/api/questions/",w))!=0:
        return "questiongetlist"
    return ""

