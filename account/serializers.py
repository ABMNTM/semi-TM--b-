from rest_framework.serializers import ModelSerializer , Serializer
from rest_framework import serializers
from django.contrib.auth.models import User
from usualFuncs import generator


class UserCreateSerializer(ModelSerializer):
    """
    This serializer is for Create users.
    """
    class Meta:
        model = User
        fields = ('id' , 'username', 'password', 'first_name' , 'last_name' , 'email')
        extra_kwargs = {
            'id'       : generator(read_only = True),
            'username' : generator(required = True),
            'password' : generator(required = True , write_only = True),
        }

class UserRUDSerializer(ModelSerializer):
    """
    This serializer implemented for
    RUD (Retreve , Update , Delete) operation.
    """
    class Meta:
        model = User
        fields = ('id' , 'username', 'first_name' , 'last_name' , 'email')
        extra_kwargs = {
            'id' : generator(read_only = True),
        }

class UserPasswordUpdateSerializer(Serializer):
    """
    A simple serializer for password update.
    """
    model = User

    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)