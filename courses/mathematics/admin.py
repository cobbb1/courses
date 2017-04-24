from django.contrib import admin



from .models import Question
from .models import Chapter
from .models import Neuron
from .models import Connect
from .models import Users
from .models import UserNeuron
from .models import Action,UserQuestion
from .models import Keyword
from .models import Suggestion
from .models import QuestionSuggestion
from .models import Useful
from .models import Hardness
from .models import Prefer
admin.site.register(Neuron)
admin.site.register(Question)
admin.site.register(Chapter)
admin.site.register(Connect)
admin.site.register(Users)
admin.site.register(UserNeuron)
admin.site.register(Action)
admin.site.register(UserQuestion)
admin.site.register(Keyword)
admin.site.register(Suggestion)
admin.site.register(QuestionSuggestion)
admin.site.register(Useful)
admin.site.register(Hardness)
admin.site.register(Prefer)