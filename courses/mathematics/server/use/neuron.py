__author__ = 'Administrator'





from mathematics.models import UserNeuron,UserQuestion
from django.db.models import Count
from django.db.models import Min,Sum

def neuron(userid,questionid):
    e = questionid.linkneuron.all()
    for z in e:
        print(questionid.id)
        m = UserNeuron.objects.filter(neuronid=z.id,userid=userid.id)
        print(m)
        n = z.question_set.all()
        w = UserQuestion.objects.filter(questionid__linkneuron__id=z.id,userid=userid.id,correct="wrong",righte=1)
        l = 0
        for i in w:
            l = l + 1/float(i.questionid.linkneuron.count())
        o = UserQuestion.objects.filter(questionid__linkneuron__id=z.id,userid=userid.id,correct="right",righte=1).aggregate(w=Count("questionid"))
        print(o["w"])
        print(l)
        l = float(o["w"]-l)/n.count()
        if m.count()==0:
            j = UserNeuron(neuronid=z,userid=userid,familiar=l)
            j.save()
        else:
            m.update(familiar=l)
    return 0
