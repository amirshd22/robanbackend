from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('profile_update/', views.UserProfileUpdate, name="profile_update"), 
    path('profile_update/photo/', views.ProfilePictureUpdate.as_view(), name="profile_update_photo"), 
    path('delete-profile/', views.delete_user, name="delete-user"),
    path('profile_update/delete/', views.ProfilePictureDelete, name="profile_delete_photo"), 
    path('profile_update/interests/', views.update_interests, name='update_interests'),
    path("create-member/", views.createMember , name="createMember"),
    path("member_update/interests/<str:id>/", views.updateMemberInterest, name="updateMemberInterests")
]
