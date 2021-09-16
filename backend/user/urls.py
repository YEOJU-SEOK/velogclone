from django.urls import path, include
from .views import CurrentUserAPIView, UserListAPIView, ProfileUpdateAPIView

urlpatterns = [
    path('currentuser/', CurrentUserAPIView.as_view()),
    path('userlist/', UserListAPIView.as_view()),
    path("profileupdate/<int:user_pk>/", ProfileUpdateAPIView.as_view()),

]