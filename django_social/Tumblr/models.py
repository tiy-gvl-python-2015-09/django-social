from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    following = models.ManyToManyField("self", symmetrical=False)


class Entry(models.Model):
    id = models.ForeignKey(Profile)
    time_signature = models.DateTimeField(auto_now_add=True)
    content_text = models.TextField()
    content_link = models.URLField()
    content_video = models.URLField()
    content_photo = models.ImageField()
    content_audio = models.URLField()
    content_quote = model.TextField()
    content_chat = model.TextField()
    re_blog = model.ManyToManyField("self", symmetrical=False)

class Home_Page(models.Model):
    user = models.ForeignKey(Profile)
    contributors = models.ForeignKey(Profile.following)
    posts = models.ForeignKey(Entry, id=Profile.following)

class Personal_Blog(models.Model):
    user = models.ForeignKey(Profile)
    posts = models.ForeignKey(Entry)
    likes = models.ManyToManyField(Entry)
    followers = models.ForeignKey(Profile.following, id='self')

class Explore(models.Model):
    posts = model.ForeignKey(Entry)
    trending_searches = model.ForeignKey(Trending)

class Trending(models.Model):
    posts = model.ForeignKey(Entry, id=most_liked)

