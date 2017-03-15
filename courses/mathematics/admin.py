from django.contrib import admin

from .models import Question
from .models import Neuron

admin.site.register(Neuron)
admin.site.register(Question)