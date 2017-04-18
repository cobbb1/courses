__author__ = 'Administrator'


from django.core import serializers
from django.http import HttpResponse
from mathematics.models import Connect,Neuron



def getlist(request,chapter_id):
    connects = Connect.objects.filter(begin__chapter=chapter_id,ending__chapter=chapter_id)
    e = Neuron.objects.filter(chapter_id="5")
    for z in e:
        m = z.x
        i = z.y
        z.x=i
        z.y=m
        z.save()
    return HttpResponse(serializers.serialize("json",connects),content_type="applcation/text")