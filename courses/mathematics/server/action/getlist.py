__author__ = 'Administrator'






from mathematics.models import Action
from mathematics.server.getresponse import get_response
from django.forms.models import model_to_dict


def getlist(request):
    w = Action.objects.all()
    z = model_to_dict(w)
    e = open("theall/ew.csv","w")
    for l in z[0]:
        e.write(l+",")
    e.write("\n")
    for w in z:
        for p,o in w:
            e.write(o+",")
        e.write("\n")
    e.close()
    return get_response(200,"lala.ust.hk:8000/theall/ew.csv",{})
