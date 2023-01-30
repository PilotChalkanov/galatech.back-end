from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.auth_app.models import GalaTechProfile, GalaTechUser


class UserProfileSerializer(serializers.ModelSerializer):
    """Product JSON serializer"""

    class Meta:
        model = GalaTechProfile
        exclude = ('user_id')


# Serializer to Register User
class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer to Register User
    """

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=GalaTechUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = GalaTechUser
        fields = ('email', 'password', 'password2',
                  )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = GalaTechUser.objects.create(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
