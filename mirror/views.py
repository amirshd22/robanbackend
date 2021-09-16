from django.shortcuts import render , get_object_or_404
from .models import Mirror
from rest_framework.response import Response
from .serializers import MirrorSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['POST'])
def createMirror(request):
    data = request.data
    mirror = Mirror.objects.create(
        name=data.get("name")
    )
    serializer = MirrorSerializer(mirror , many=False)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes((IsAuthenticated,))
def setMirrorUser(request, name):
    user = request.user
    data = request.data
    try:
        mirror = Mirror.objects.get(name=name)
        mirror.token = data.get("token")
        mirror.user = user
        mirror.save()
        serializer = MirrorSerializer(mirror , many=False)
        return Response(serializer.data)
    except Exception as e:
         return Response({'details': f"{e}"},status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def getMirror(request, name):
    mirror = Mirror.objects.get(name=name)
    serializer = MirrorSerializer(mirror , many=False)
    return Response(serializer.data)
