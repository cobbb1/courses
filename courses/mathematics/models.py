from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    code = models.CharField(max_length=100,primary_key=True)
    problem = models.TextField()
    problempicture1 = models.ImageField(blank=True,null=True)
    problempicture2 = models.ImageField(blank=True,null=True)
    problempicture3 = models.ImageField(blank=True,null=True)
    problempicture4 = models.ImageField(blank=True,null=True)
    problempicture5 = models.ImageField(blank=True,null=True)
    problempicture6 = models.ImageField(blank=True,null=True)
    choicesa = models.TextField(blank=True,null=True)
    choicesb = models.TextField(blank=True,null=True)
    choicesc = models.TextField(blank=True,null=True)
    choicesd = models.TextField(blank=True,null=True)
    choicese = models.TextField(blank=True,null=True)
    choicesf = models.TextField(blank=True,null=True)
    choicepicturea = models.ImageField(blank=True,null=True)
    choicepictureb = models.ImageField(blank=True,null=True)
    choicepicturec = models.ImageField(blank=True,null=True)
    choicepictured = models.ImageField(blank=True,null=True)
    choicepicturee = models.ImageField(blank=True,null=True)
    choicepicturef = models.ImageField(blank=True,null=True)
    answer = models.TextField()
    solutions = models.TextField()
    linkneuron = models.FloatField(blank=True,null=True)
    linkability = models.FloatField(blank=True,null=True)
    linkpersonaility = models.FloatField(blank=True,null=True)
    errors = models.TextField(blank=True,null=True)
    alternativesolutions = models.TextField(blank=True,null=True)
    messagefailure = models.TextField()
    messagesuccess = models.TextField()
    sensitivity = models.FloatField(blank=True,null=True)
    gussingparameter = models.FloatField(blank=True,null=True)
    difficulty = models.FloatField()
    twinproblems = models.ManyToManyField("self",blank=True,null=True)
