from django.shortcuts import render
from rest_framework import response, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.auth_app.serializers import UserRegisterSerializer, UserProfileSerializer


class UserRegisterView(CreateAPIView):
    """User Registration view"""
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)


class CreateUserProfileView(APIView):
    """
    User profile create view
    should add user_id to profile
    """

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.id)
        return Response(status=status.HTTP_201_CREATED)