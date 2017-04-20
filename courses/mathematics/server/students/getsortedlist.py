__author__ = 'Administrator'

from django.http import HttpResponse
from django.core import serializers
from mathematics.models import Question,Neuron,Users,Chapter,UserQuestion

def getSortedStudentList(request):

    questions_in_one_chapter = Question.objects()
    questions_in_one_chapter_in_one_student = UserQuestion.objects()
    all_students = Users.objects().only("id","names")
    if request.GET.has_key('chapter'):
        # get all the question ids in one or some chapter, since the chapter id is char field
        questions_in_one_chapter = Question.objects.filter(linkneuron=Neuron.objects.filter(chapter=request.GET["chapter"])).only("id")
        print(questions_in_one_chapter)

        # get all the question feedbacks in these chapters
        questions_in_one_chapter_in_all_student = UserQuestion.filter(questionid__in = questions_in_one_chapter)
        print(questions_in_one_chapter_in_all_student)

        # calculate each students' correctness in these chapters
        for student in all_students:
            student









    w = Question.objects.only("id","category","code","difficulty","sensitivity")
    if request.GET.has_key("neurons"):
        w = Question.objects.filter(linkneuron=Neuron.objects.filter(id=int(request.GET["neurons"]))[0]).only("id", "category", "code", "difficulty", "sensitivity")
        print(w)
    if request.GET.has_key("difficulty"):
        w = w.filter(difficulty=int(request.GET["difficulty"]))
        print(w)
    return HttpResponse(serializers.serialize("json", w, fields=("id","category","code","difficulty","sensitivity")), content_type="application/json")