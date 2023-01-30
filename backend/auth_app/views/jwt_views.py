from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """JWT token serializer
     returns a token with additional:
     username
     user_id
     """

    def validate(self, attrs):
        data = super().validate(attrs)

        data['username'] = self.user.email
        data['user_id'] = self.user.id
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
