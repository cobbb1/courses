__author__ = 'Administrator'



from mathematics.models import Users,UserQuestionLikes
from mathematics.server.getresponse import get_response
from django.core.serializers import serialize

def getquestionlikes(reuqest,userid):
    w = Users.objects.filter(id=int(userid))
    if w.count()==0:
        return get_response(200,"z",{})
    e = UserQuestionLikes.objects.filter(userid=int(userid))
    return get_response(200,serialize("json",e),{})
