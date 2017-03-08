from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    code = models.CharField(max_length=100,primary_key=True)
    categorychoice = (
        (1,"exercies"),
        (2,"example"),
        (3,"diy")
    )
    category = models.IntegerField(choices=categorychoice)
    problem = models.TextField()
    problempicture1 = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    problempicture2 = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    problempicture3 = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    problempicture4 = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    problempicture5 = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    problempicture6 = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    choicesa = models.TextField(blank=True,null=True)
    choicesb = models.TextField(blank=True,null=True)
    choicesc = models.TextField(blank=True,null=True)
    choicesd = models.TextField(blank=True,null=True)
    choicese = models.TextField(blank=True,null=True)
    choicesf = models.TextField(blank=True,null=True)
    choicepicturea = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    choicepictureb = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    choicepicturec = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    choicepictured = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    choicepicturee = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    choicepicturef = models.ImageField(blank=True,null=True,upload_to="theall/image/")
    answerchoice = (
        ("A","A"),
        ("B","B"),
        ("C","C"),
        ("D","D"),
        ("E","E"),
        ("F","F")
    )
    answer = models.CharField(choices=answerchoice,max_length=200)
    solutionspicture1 = models.ImageField(null=True,blank=True,upload_to="theall/image")
    solutionspicture2 = models.ImageField(null=True,blank=True,upload_to="theall/image")
    solutionspicture3 = models.ImageField(null=True,blank=True,upload_to="theall/image")
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
