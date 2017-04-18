__author__ = 'Administrator'


from django.core import serializers
from django.http import HttpResponse
from mathematics.models import Connect,Neuron



def getlist(request,chapter_id):
    connects = Connect.objects.filter(begin__chapter=chapter_id,ending__chapter=chapter_id)
    return HttpResponse(serializers.serialize("json",connects),content_type="applcation/text")