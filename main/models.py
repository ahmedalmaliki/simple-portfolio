from django.db import models

# Create your models here.

class Experience(models.Model):
    startYear = models.IntegerField()
    endYear = models.IntegerField()
    describe = models.CharField(max_length= 3000)

class Skills(models.Model):
    skillName = models.CharField(max_length= 225)

class Languages(models.Model):
    language = models.CharField(max_length= 225)

class User(models.Model):
    Fullname = models.CharField(max_length= 225)
    Profile = models.CharField(max_length= 2000)
    Address = models.CharField(max_length= 300)
    Phone = models.CharField(max_length= 225)
    Email = models.CharField(max_length= 225)
    Website = models.CharField(max_length= 225)
class Projects(models.Model):
    projectName = models.CharField(max_length= 225)
    projectLink = models.CharField(max_length= 225)
    projectDescription = models.CharField(max_length= 225)
    