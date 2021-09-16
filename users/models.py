from django.db import models
from django.contrib.auth.models import User
import uuid



# Create your models here.
class TopicTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)
    
    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(blank=True, null=True, default='default.png')
    faceRecognition_pic = models.ImageField(blank=True, null=True)
    character = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=200, null=True)
    birth_day_date = models.CharField(max_length=500, null=True)
    interests = models.ManyToManyField(TopicTag, related_name='topic_interests', blank=True)
    phoneNumber = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
  
    def __str__(self):
        return str(self.user.username)

class Member(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    username = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(blank=True, null=True, default='default.png')
    faceRecognition_pic = models.ImageField(blank=True, null=True)
    character = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=200, null=True)
    birth_day_date = models.CharField(max_length=500, null=True)
    interests = models.ManyToManyField(TopicTag, related_name='topic_members_interests', blank=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)