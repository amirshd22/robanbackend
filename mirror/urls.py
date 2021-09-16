from django.urls import path
from . import views

urlpatterns= [
    path("createMirror/" , views.createMirror, name="createMirror"),
    path("setMirrorUser/<str:name>/", views.setMirrorUser , name="setMirrorUser"),
    path("getMirror/<str:name>/", views.getMirror , name="getMirror"),

]