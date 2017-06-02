__author__ = 'Administrator'



from mathematics.server.getresponse import get_response
from mathematics.models import Users,UserQuestion


def wez(request,userid):
    e = Users.objects.filter(id=int(userid))
    if e.count()==0:
        return get_response(200,"z",{})
    w = UserQuestion.objects.filter(userid=int(userid)).update(righte=0)
    return get_response(200,"e",{})