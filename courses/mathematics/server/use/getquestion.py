__author__ = 'Administrator'





from django.core.serializers import serialize
from mathematics.server.getresponse import get_response
from mathematics.models import UserQuestion


def getquestion(request,userid):
    e = UserQuestion.objects.filter(righte=1,userid=userid)
    return get_response(200,serialize("json",e),{})
