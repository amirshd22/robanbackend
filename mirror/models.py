from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Mirror(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250,null=True)
    token = models.TextField(null=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    def __str__(self):
        return str(self.id)