from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from .serializers import ProfileSerializer, UserSerializerWithToken, UserSerializer
from .models import Profile


class CurrentUserAPIView(RetrieveAPIView):
    """
    현재 유저 호출 APIView
    """
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)


#TODO 회원가입으로 class명 수정예정
class UserListAPIView(CreateAPIView):
    """
    회원가입 APIView(with TOKEN)
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializerWithToken

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#TODO 목적에 맞는 class명 수정
class ProfileUpdateAPIView(UpdateAPIView):
    """
    프로필 업데이트 APIView
    """
    lookup_field = "user_pk"
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
