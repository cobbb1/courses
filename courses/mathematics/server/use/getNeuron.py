__author__ = 'Administrator'




from mathematics.models import UserNeuron
from django.core import serializers
from django.http import HttpResponse

def getNeuron(request,user_id,chapter_id):
    e = UserNeuron.objects.filter(userid=user_id,neuronid__chapter=chapter_id)
    return HttpResponse(serializers.serialize("json",e),content_type="application/json")