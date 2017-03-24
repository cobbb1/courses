from django.contrib import admin

from .models import Question
from .models import Chapter
from .models import Neuron
from .models import Connect
from .models import Users
from .models import UserNeuron
admin.site.register(Neuron)
admin.site.register(Question)
admin.site.register(Chapter)
admin.site.register(Connect)
admin.site.register(Users)
admin.site.register(UserNeuron)