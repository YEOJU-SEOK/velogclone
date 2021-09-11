from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
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

