from django.db import models
from django.contrib.auth.models import User
import uuid



# Create your models here.




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(blank=True, null=True, default='default.png')
    faceRecognition_pic = models.ImageField(blank=True, null=True)
    gender = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
  
    def __str__(self):
        return str(self.user.username)