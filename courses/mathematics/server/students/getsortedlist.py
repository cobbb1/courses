__author__ = 'Administrator'

from django.http import HttpResponse
from django.core import serializers
from mathematics.models import Question,Neuron,Users,Chapter,UserQuestion
from mathematics.server.getresponse import get_response
import json

def getSortedStudentList(request):

    questions_in_one_chapter = Question.objects.all()
    questions_in_one_chapter_of_all_student = UserQuestion.objects.all()
    questions_in_one_chapter_of_one_student = UserQuestion.objects.all()
    all_students = Users.objects.only("id","names")
    if request.GET.has_key('chapter'):
        # get all the question ids in one or some chapter, since the chapter id is char field
        questions_in_one_chapter = Question.objects.filter(linkneuron__in = Neuron.objects.filter(chapter=request.GET["chapter"])).only("id")
        print(questions_in_one_chapter)

        # get all the question feedbacks in these chapters
        questions_in_one_chapter_of_all_student = UserQuestion.objects.filter(questionid__in = questions_in_one_chapter)
        print(questions_in_one_chapter_of_all_student)

        result = []
        record = {}

        # calculate each students' correctness in these chapters
        for student in all_students:
            # get all the question feedbacks in these chapters of this student
            questions_in_one_chapter_of_one_student = questions_in_one_chapter_of_all_student.filter(userid = student.id)
            # calculate the correctness
            count = 0.0
            total = 0.0
            for userquestion in questions_in_one_chapter_of_one_student:
                if userquestion.correct == "right":
                    count += 1.0
                total += 1.0

            if total != 0:
                accuracy = count / total # test if this is double
            else:
                accuracy = 0

            record = {"userid":student.id,"username":student.names,"accuracy":accuracy,"right":count,"wrong":total-count,"count":count}
            result.append(record)
        print(result)

        # do sorting according to accuracy in descending order
        sorted(result, key = lambda temp:temp['accuracy'])

        # return the result in json format
        return HttpResponse(json.dumps(result), content_type="application/json")

def getDoneRecord(request):
    userid = 0
    if request.GET.has_key('userid') == 0:
        return get_response(403, '{"message":"no userid"}', {})
    else:
        userid = int(request.GET["userid"])
        test = Users.objects.filter(id = userid)
        if test.count() == 0:
            return get_response(403, '{"message":"no such user"}', {})

        userquestion = UserQuestion.objects.filter(userid = userid)
        questions = Question.objects.all()
        result_list = []
        for question in questions:
            # no .values, it is an object, use . instead of [], [] is for dictionary
            questionid = question.id
            test = userquestion.filter(questionid = questionid)
            result_item = {}
            if test.count() == 0:
                result_item={"questionid":questionid,"isdone":False, "result":""}
            else:
                result = test[0].correct
                result_item = {"questionid": questionid, "isdone": True, "result":result}
            result_list.append(result_item)

        return  HttpResponse(json.dumps(result_list), content_type="application/json")

