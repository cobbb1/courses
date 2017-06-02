__author__ = 'Administrator'





from mathematics.models import Users,Question,UserQuestionLikes
from mathematics.server.getresponse import get_response


def questionlikes(request,userid,questionid):
    w = Question.objects.filter(id=int(questionid))
    if w.count()==0:
        return get_response(200,"z",{})
    e = Users.objects.filter(id=int(userid))
    if e.count()==0:
        return get_response(200,"z",{})
    p = UserQuestionLikes.objects.filter(userid=int(userid),questionid=int(questionid))
    if p.count()==0:
        i = UserQuestionLikes(userid=e[0],questionid=w[0])
        i.save()
        return get_response(200,"okl",{})
    else:
        return get_response(200,"w",{})