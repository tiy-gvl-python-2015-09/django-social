from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    photo = models.ImageField()
    connections = models.ManyToManyField("self")
    skills = models.TextField()


class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    size = models.IntegerField(max_length=100)
    location = models.CharField(max_length=100)
    followers = models.ManyToManyField(Person)


class Experience(models.Model):
    user = models.ForeignKey(Person)
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    dates = models.DateField()
    description = models.TextField()


class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    followers = models.ManyToManyField(Person)


class Education(models.Model):
    user = models.ForeignKey(Person)
    school = models.ForeignKey(School)
    dates = models.DateField()
    degree = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    activities = models.TextField()
    description = models.TextField()

