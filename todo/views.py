from django.urls.resolvers import LocaleRegexDescriptor
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializers
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getUserTodo(request):
    user = request.user
    all_todo = Todo.objects.filter(user=user).order_by("-created")
    serializer = TodoSerializers(all_todo, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getTargetedTodo(request , pk):
    user = request.user
    todo = get_object_or_404(Todo , pk=pk)
    serializer = TodoSerializers(todo, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def editTodo(request, pk): 
    user= request.user
    data= request.data
    try:
        todo = Todo.objects.get(id=pk)
        if user == todo.user:
            todo.title = data.get("title")
            todo.content = data.get("content")
            todo.when_to_finish  = data.get("when_to_finish")
            todo.save()
            serializer = TodoSerializers(todo , many=False)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
         return Response({'details': f"{e}"},status=status.HTTP_204_NO_CONTENT)


@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def deleteTodo(request, pk):
    user= request.user
    try:
        todo = get_object_or_404(Todo , pk=pk)
        print(todo)
        if user == todo.user:
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def createTodo(request):
    user= request.user
    data = request.data
    todo = Todo.objects.create(
        title = data.get("title"),
        user= user,
        content = data.get("content"),
        when_to_finish = data.get("when_to_finish")
    )
    todo.save()
    serializer = TodoSerializers(todo , many=False)
    return Response(serializer.data)
    