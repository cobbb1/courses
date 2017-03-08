from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    code = models.CharField(max_length=100,primary_key=True)
    problem = models.TextField()
    problempicture1 = models.ImageField(blank=True,null=True,upload_to="image/")
    problempicture2 = models.ImageField(blank=True,null=True,upload_to="image/")
    problempicture3 = models.ImageField(blank=True,null=True,upload_to="image/")
    problempicture4 = models.ImageField(blank=True,null=True,upload_to="image/")
    problempicture5 = models.ImageField(blank=True,null=True,upload_to="image/")
    problempicture6 = models.ImageField(blank=True,null=True,upload_to="image/")
    choicesa = models.TextField(blank=True,null=True)
    choicesb = models.TextField(blank=True,null=True)
    choicesc = models.TextField(blank=True,null=True)
    choicesd = models.TextField(blank=True,null=True)
    choicese = models.TextField(blank=True,null=True)
    choicesf = models.TextField(blank=True,null=True)
    choicepicturea = models.ImageField(blank=True,null=True,upload_to="image/")
    choicepictureb = models.ImageField(blank=True,null=True,upload_to="image/")
    choicepicturec = models.ImageField(blank=True,null=True,upload_to="image/")
    choicepictured = models.ImageField(blank=True,null=True,upload_to="image/")
    choicepicturee = models.ImageField(blank=True,null=True,upload_to="image/")
    choicepicturef = models.ImageField(blank=True,null=True,upload_to="image/")
    answerchoice = (
        ("A","A"),
        ("B","B"),
        ("C","C"),
        ("D","D"),
        ("E","E"),
        ("F","F")
    )
    answer = models.CharField(choices=answerchoice,max_length=200)
    solutions = models.TextField()
    linkneuron = models.FloatField(blank=True,null=True)
    linkability = models.FloatField(blank=True,null=True)
    linkpersonaility = models.FloatField(blank=True,null=True)
    errors = models.TextField(blank=True,null=True)
    alternativesolutions = models.TextField(blank=True,null=True)
    messagefailure = models.TextField(blank=True,null=True)
    messagesuccess = models.TextField(blank=True,null=True)
    sensitivity = models.FloatField(blank=True,null=True)
    gussingparameter = models.FloatField(blank=True,null=True)
    difficultchoice = (
        (1,"easy"),
        (2,"not very easy"),
        (3,"medium"),
        (4,"a little difficult"),
        (5,"difficult")
    )
    difficulty = models.FloatField(choices = difficultchoice)
    twinproblems = models.ManyToManyField("self",blank=True,null=True)
