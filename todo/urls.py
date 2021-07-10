from django.urls import path
from . import views

urlpatterns = [
    path("createTodo/", views.createTodo, name="createTodo"),
    path("getTodo/", views.getUserTodo, name="getTodo"),
    path("deleteTodo/<str:pk>/", views.deleteTodo, name="deleteTodo"),
    path("editTodo/<str:pk>/", views.editTodo, name="editTodo"),
    path("getTargetedTodo/<str:pk>/", views.getTargetedTodo, name="getTargetedTodo")

]