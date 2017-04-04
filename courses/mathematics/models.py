from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    names = models.CharField(max_length=200)
    question = models.ManyToManyField("Question",through_fields=("userid","questionid"),through="UserQuestion")
    neuron = models.ManyToManyField("Neuron",  through_fields=("userid","neuronid"),through="UserNeuron")
    token = models.CharField(max_length=100,blank=True,null=True)
    login = models.DateTimeField(blank=True)



class UserQuestion(models.Model):
    userid = models.ForeignKey(Users,on_delete=models.CASCADE)
    questionid = models.ForeignKey("Question",on_delete=models.CASCADE)
    time = models.DateTimeField()
    e = models.IntegerField()
    answer = models.CharField(max_length=100)
    right=models.CharField(max_length=100)


class UserNeuron(models.Model):
    userid = models.ForeignKey(Users,on_delete = models.CASCADE)
    neuronid = models.ForeignKey("Neuron",on_delete = models.CASCADE)
    familiar = models.FloatField()

class Connect(models.Model):
    def __str__(self):
        return str(self.begin) + "-" + str(self.end)
    begin = models.ForeignKey('Neuron',on_delete=models.CASCADE,related_name="+")
    ending = models.ForeignKey('Neuron',on_delete=models.CASCADE,related_name="+")
    detail = models.CharField(max_length=200,null=True,blank=True)

class Neuron(models.Model):
    def __str__(self):
        return self.title + "-" + self.chapter
    title = models.CharField(max_length=200)
    category = (
        (1,"1"),
        (2,"2"),
        (3,"3")
    )
    detail = models.TextField()
    to = models.ManyToManyField('self',through_fields=("begin","ending"),through=Connect,symmetrical=False)
    x = models.FloatField()
    y = models.FloatField()
    a = models.FloatField()
    b = models.FloatField()
    names = models.CharField(max_length=200)
    bolder = models.IntegerField(blank=True,bull=True)
    chapter = models.ForeignKey('Chapter',on_delete=models.CASCADE)




class Chapter(models.Model):
    def __str__(self):
        return self.id
    id = models.CharField(max_length=100,primary_key=True)




class Question(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    categorychoice = (
        (1,"Expl"),
        (2,"Exer"),
        (3,"Prob"),
        (4, "DIY"),
        (5,"Qui")
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
    answerchoices = (
        ("A","A"),
        ("B","B"),
        ("C","C"),
        ("D","D"),
        ("E","E"),
        ("F","F"),
        ("G","G"),
    )
    answer = models.CharField(choices=answerchoices,max_length=100)
    solutionspicture1 = models.ImageField(null=True,blank=True,upload_to="theall/image")
    solutionspicture2 = models.ImageField(null=True,blank=True,upload_to="theall/image")
    solutionspicture3 = models.ImageField(null=True,blank=True,upload_to="theall/image")
    solutions = models.TextField()
    linkneuron = models.ManyToManyField(Neuron,blank=True)
    linkability1 = models.FloatField(null=True,blank=True)
    linkability2 = models.FloatField(null=True,blank=True)
    linkability3 = models.FloatField(null=True,blank=True)
    linkability4 = models.FloatField(null=True,blank=True)
    linkability5 = models.FloatField(null=True,blank=True)
    linkability6 = models.FloatField(null=True,blank=True)
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
    difficulty = models.IntegerField(choices = difficultchoice)
    rightproblems = models.ManyToManyField("self",blank=True)
    wrongproblems = models.ManyToManyField("self",blank=True)
    twinproblems = models.ManyToManyField("self",blank=True)
    def __unicode__(self):
        # print (self.category)
        # print(self.categorychoice[self.category])
        return self.categorychoice[self.category-1][1]+self.code #tuple inside tuples
