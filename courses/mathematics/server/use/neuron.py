__author__ = 'Administrator'





from mathematics.models import UserNeuron,UserQuestion
from django.db.models import Count

def neuron(userid,questionid):
    e = questionid.linkneuron.all()
    for z in e:
        m = UserNeuron.objects.filter(neuronid=z.id,userid=userid.id)
        n = z.question_set.all()
        print(n)
        w = UserQuestion.objects.filter(questionid__linkneuron__id=z.id,userid=userid.id,correct="right").values("questionid").annotate(counts=Count(questionid,distinct=True))
        print(w)
        l = float(len(w))/n.count()
        if m.count()==0:
            j = UserNeuron(neuronid=z,userid=userid,familiar=l)
            j.save()
        else:
            m.update(familiar=l)
    return 0
