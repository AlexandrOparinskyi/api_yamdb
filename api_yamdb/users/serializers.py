from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .validators import username_is_not_me, username_is_unique

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')


class MeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')


class UserRegistration(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=60,
        required=True,
        validators=[username_is_unique, username_is_not_me]
    )
    email = serializers.EmailField(
        max_length=60,
        required=True, 
    )
    
    class Meta:
        model = User
        fields = ('username', 'email')


class UserCodeConfirm(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=60,
        required=True
    )
    code_confirm = serializers.CharField(
        max_length=60,
        required=True, 
    )
    
    class Meta:
        model = User
        fields = ('username', 'code_confirm')