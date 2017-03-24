__author__ = 'Administrator'


from django.core import serializers
from django.http import HttpResponse
from mathematics.models import Connect,Neuron

from django.db.models import F


def getlist(request,chapter_id):
    neurons = Neuron.objects.filter(chapter=chapter_id)
    return HttpResponse(serializers.serialize("json",neurons),content_type="applcation/text")