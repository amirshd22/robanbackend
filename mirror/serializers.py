from rest_framework import serializers
from .models import Mirror 

class MirrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mirror
        fields = "__all__"

