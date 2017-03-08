from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    code = models.CharField(max_length=100,primary_key=True)
    problem = models.TextField()
    problempicture1 = models.ImageField(null=True)
    problempicture2 = models.ImageField(null=True)
    problempicture3 = models.ImageField(null=True)
    problempicture4 = models.ImageField(null=True)
    problempicture5 = models.ImageField(null=True)
    problempicture6 = models.ImageField(null=True)
    choicesa = models.TextField(null=True)
    choicesb = models.TextField(null=True)
    choicesc = models.TextField(null=True)
    choicesd = models.TextField(null=True)
    choicese = models.TextField(null=True)
    choicesf = models.TextField(null=True)
    choicepicturea = models.ImageField(null=True)
    choicepictureb = models.ImageField(null=True)
    choicepicturec = models.ImageField(null=True)
    choicepictured = models.ImageField(null=True)
    choicepicturee = models.ImageField(null=True)
    choicepicturef = models.ImageField(null=True)
    answer = models.TextField()
    solutions = models.TextField()
    linkneuron = models.FloatField()
    linkability = models.FloatField()
    linkpersonaility = models.FloatField()
    errors = models.TextField()
    alternativesolutions = models.TextField()
    messagefailure = models.TextField()
    messagesuccess = models.TextField()
    sensitivity = models.FloatField()
    gussingparameter = models.FloatField()
    difficulty = models.FloatField()
    twinproblems = models.ManyToManyField("self")
