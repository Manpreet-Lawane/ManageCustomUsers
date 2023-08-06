from rest_framework import serializers
from ManageCustomUsersApp.models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'user_type')


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class LinkSerializer(serializers.Serializer):
    title = serializers.CharField()
    address = serializers.CharField()