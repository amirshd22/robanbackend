from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Todo
from users.serializers import UserProfileSerializer


class TodoSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta: 
        model = Todo
        fields = '__all__'
    
    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializer(user, many=False)
        return serializer.data
