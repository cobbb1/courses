__author__ = 'Administrator'






from mathematics.models import Users,UserQuestion,Question
from mathematics.server.getresponse import get_response


def evaluate(request,userid):
    z = UserQuestion.objects.filter(userid=userid,correct="wrong")
    w = UserQuestion.objects.filter(userid=userid,correct="right")
    m1=0
    m2=0
    m3=0
    m4=0
    m5=0
    m6=0
    for l in z:
        m1 = m1 - l.questionid.linkability1
        m2 = m2 - l.questionid.linkability2
        m3 = m3 - l.questionid.linkability3
        m4 = m4 - l.questionid.linkability4
        m5 = m5 - l.questionid.linkability5
        m6 = m6 - l.questionid.linkability6
    for i in w:
        m1 = m1 + i.questionid.linkability1
        m2 = m2 + i.questionid.linkability2
        m3 = m3 + i.questionid.linkability3
        m4 = m4 + i.questionid.linkability4
        m5 = m5 + i.questionid.linkability5
        m6 = m6 + i.questionid.linkability6
    j = w.count()+z.count()
    if 0!=w.count()+z.count():
        m1 = float(m1)/j
        m2 = float(m2)/j
        m3 = float(m3)/j
        m4 = float(m4)/j
        m5 = float(m5)/j
        m6 = float(m6)/j
    o = ""
    o = o + '{"1":'+str(m1)+','
    o = o + '"2":'+str(m2)+','
    o = o + '"3":'+str(m3)+','
    o = o + '"4":'+str(m4)+','
    o = o + '"5":'+str(m5)+','
    o = o + '"6":'+str(m6)+','

    p = UserQuestion.objects.filter(questionid__category=1,userid=userid).count()
    w = Question.objects.filter(category=1).count()
    o = o + '"example":'+str(p)+','+'"examplecount":' + str(w)

    p = UserQuestion.objects.filter(questionid__category=2,userid=userid).count()
    w = Question.objects.filter(category=2).count()
    o = o + '"exercise":'+str(p)+','+'"exercisecount":' + str(w)

    p = UserQuestion.objects.filter(questionid__category=3,userid=userid).count()
    w = Question.objects.filter(category=3).count()
    o = o + '"problem":'+str(p)+','+'"problemcount":' + str(w)

    p = UserQuestion.objects.filter(questionid__category=4,userid=userid).count()
    w = Question.objects.filter(category=4).count()
    o = o + '"diy":'+str(p)+','+'"diycount":' + str(w)

    p = UserQuestion.objects.filter(questionid__category=5,userid=userid).count()
    w = Question.objects.filter(category=5).count()
    o = o + '"quizs":'+str(p)+','+'"quizscount":' + str(w)


    o = o + '}'



    return get_response(200,o,{})