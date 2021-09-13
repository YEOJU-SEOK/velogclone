from django.urls import path, include
from .views import CurrentUserAPIView, UserListAPIView, ProfileUpdateAPIView

urlpatterns = [
    path('currentuser/', CurrentUserAPIView.as_view()),
    path('userlist/', UserListAPIView.as_view()),
<<<<<<< HEAD
    path("profileupdate/<int:user_pk>/", ProfileUpdateAPIView.as_view()),
=======
    path("profileupdate/<int:user_pk>ㅊㅊ/", ProfileUpdateAPIView.as_view()),
>>>>>>> d5f2d071420f2d770d2d9ec5da46f48b06540f2d
]