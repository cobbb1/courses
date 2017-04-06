__author__ = 'Administrator'





from mathematics.models import UserNeuron,UserQuestion
from django.db.models import Count

def neuron(userid,questionid):
    e = questionid.linkneuron.all()
    for z in e:
        m = UserNeuron.objects.filter(neuronid=z.id,userid=userid.id)
        n = UserQuestion.objects.filter(questionid__linkneuron__id=z.id,userid=userid.id).annotate(counts=Count(questionid,distinct=True))
        print(n[0])
        w = UserQuestion.objects.filter(questionid__linkneuron__id=z.id,userid=userid.id,correct="right").annotate(counts=Count(questionid,distinct=True))
        print(w[0])
        if m.count()==0:
            j = UserNeuron(neuronid=z,userid=userid,familiar=float(w[0].counts)/n[0].counts)
            j.save()
        else:
            m.update(familiar=float(w[0].counts)/n[0].counts)
    return 0
