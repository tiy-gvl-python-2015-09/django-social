from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    following = models.ManyToManyField("self", symmetrical=False)
    

class Entry(models.Model):
    id = models.ForeignKey(Profile)
    time_signature = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    content_link = models.URLField()
    content_video = models.URLField()
    content_photo = models.ImageField()

class HomeFeed(models.Model):
    user = models.ForeignKey(Profile)
    contributors = models.ForeignKey(Profile.following)
    posts = models.ForeignKey(Entry, id=Profile.following)

class Personal_Blog(models.Model):
    user = models.ForeignKey(Profile)
    posts = models.ForeignKey(Entry)
    followers = models.ForeignKey(Profile.following, id='self')
