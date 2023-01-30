from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView

from backend.auth_app.serializers import UserRegisterSerializer


class UserRegisterView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        print(data)

        return response.Response(data={'username': data.get('username'),})
