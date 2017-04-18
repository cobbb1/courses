__author__ = 'Administrator'





from mathematics.models import UserNeuron,UserQuestion
from django.db.models import Count
from django.db.models import Min

def neuron(userid,questionid):
    e = questionid.linkneuron.all()
    for z in e:
        print(questionid.id)
        m = UserNeuron.objects.filter(neuronid=z.id,userid=userid.id)
        print(m)
        n = z.question_set.all()
        print(n)
        p = UserQuestion.objects.filter(question__linkneuron__id=z.id,userid=userid.id).values("time","questionid").annotate(min=Min("time"))
        w = UserQuestion.objects.filter(questionid__linkneuron__id=z.id,userid=userid.id,correct="right").values("questionid").annotate(counts=Count(questionid,distinct=True))
        print(w)
        l = float(len(w))/n.count()
        if m.count()==0:
            j = UserNeuron(neuronid=z,userid=userid,familiar=l)
            j.save()
        else:
            m.update(familiar=l)
    return 0
