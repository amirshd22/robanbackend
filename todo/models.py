from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model, ModelState, ModelStateFieldsCacheDescriptor
from django.db.models.fields import BooleanField
import uuid
# Create your models here.



class Todo(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    when_to_finish = models.CharField(max_length=500, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title
    