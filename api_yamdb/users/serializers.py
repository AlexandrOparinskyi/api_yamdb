from users.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
