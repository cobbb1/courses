__author__ = 'Administrator'

from mathematics.server.getresponse import get_response
from mathematics.models import Question,Suggestion,QuestionSuggestion,Users
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getSystemSuggestion(request):
    result = Suggestion.objects.all()
    return HttpResponse(serializers.serialize("json", result), content_type="application/json")

@csrf_exempt
def postSystemSuggestion(request):
    userid = 0
    username = ""
    comment = ""
    if request.POST.has_key("userid") == 0:
        return get_response(403, '{"message":"no userid"}', {})
    else:
        userid = request.POST["userid"]
        test = Users.objects.filter(id = userid).count()
        if test == 0:
            return get_response(403, '{"message":"no such userid"}', {})
        else:
            userid = Users.objects.filter(id = userid)[0]

    if request.POST.has_key("username") == 0:
        return get_response(403, '{"message":"no username"}', {})
    else:
        username = request.POST["username"]
        test = Users.objects.filter(names=username).count()
        if test == 0:
            return get_response(403, '{"message":"no such username"}', {})

    if request.POST.has_key("comment") == 0:
        return get_response(403, '{"message":"no comment"}', {})
    else:
        comment = request.POST["comment"]

    record = Suggestion(userid = userid, username=username, comment=comment,time=datetime.now())
    record.save()
    return get_response(200, '{"message":"upload success"}', {})

@csrf_exempt
def getQuestionSuggestion(request):

    questionid = 0
    if request.GET.has_key('questionid'):
        questionid = request.GET["questionid"]
        test = Question.objects.filter(id=questionid).count()
        if test == 0:
            return get_response(403, '{"message":"no such question"}', {})
    else:
        return get_response(403, '{"message":"no questionid"}', {})

    result = QuestionSuggestion.objects.filter(questionid = questionid)
    return HttpResponse(serializers.serialize("json", result), content_type="application/json")

@csrf_exempt
def postQuestionSuggestion(request):
    userid = 0  # cookie's id
    username = ""  # cookie's userid
    questionid = 0
    comment = ""

    if request.POST.has_key("userid") == 0:
        return get_response(403, '{"message":"no userid"}', {})
    else:
        userid = request.POST["userid"]
        test = Users.objects.filter(id=userid).count()
        if test == 0:
            return get_response(403, '{"message":"no such userid"}', {})
        else:
            userid = Users.objects.filter(id=userid)[0]

    if request.POST.has_key("username") == 0:
        return get_response(403, '{"message":"no username"}', {})
    else:
        username = request.POST["username"]
        test = Users.objects.filter(names=username).count()
        if test == 0:
            return get_response(403, '{"message":"no such username"}', {})

    if request.POST.has_key("questionid") == 0:
        return get_response(403, '{"message":"no questionid"}', {})
    else:
        questionid = request.POST["questionid"]
        test = Question.objects.filter(id=questionid).count()
        if test == 0:
            return get_response(403, '{"message":"no such question"}', {})
        else:
            questionid = Question.objects.filter(id=questionid)[0]

    if request.POST.has_key("comment") == 0:
        return get_response(403, '{"message":"no comment"}', {})
    else:
        comment = request.POST["comment"]

    # userid must be a Users instance!!! same as other foreign key
    record = QuestionSuggestion(userid=userid, username=username, comment=comment, time=datetime.now(), questionid=questionid)
    record.save()
    return get_response(200, '{"message":"upload success"}', {})