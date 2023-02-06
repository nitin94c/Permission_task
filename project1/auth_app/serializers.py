from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)


    class Meta:
        model = User
        fields = ('username','email', 'password', 'first_name', 'last_name', 'role' )

    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)
