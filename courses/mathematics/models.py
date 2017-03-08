from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    code = models.CharField(max_length=100,primary_key=True)
    problem = models.TextField()
    choices = models.TextField()
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
