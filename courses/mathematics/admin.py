from django.contrib import admin

from .models import Question
from .models import Chapter
from .models import Neuron
from .models import Connect
from .models import Users
admin.site.register(Neuron)
admin.site.register(Question)
admin.site.register(Chapter)
admin.site.register(Connect)
admin.site.register(Users)