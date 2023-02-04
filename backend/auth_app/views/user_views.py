from django.shortcuts import render
from rest_framework import response, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.auth_app.models import GalaTechProfile
from backend.auth_app.serializers import UserRegisterSerializer, UserSerializer, ProfileSerializer


class UserRegisterView(CreateAPIView):
    """User Registration view"""
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProfileView(APIView):
    """
    User profile create view
    should add user_id to profile
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        user = request.user
        profile_info = {}
        try:
            profile = GalaTechProfile.objects.get(user=user.id)
            profile_info = ProfileSerializer(profile, many=False).data
        except GalaTechProfile.DoesNotExist:
            profile_info = {

            }

        user_serializer = UserSerializer(user, many=False)

        data = {
            "email": user_serializer.data["email"],
            "profile": profile_info

        }
        return Response(data, status=200)


    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.id)
        return Response(status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = ProfileSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)


        serializer.save(user_id=request.user.id)
        return Response(status=status.HTTP_200_OK)

