from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note
# Django uses ORM(Object Relational Mapping)
# Maps python objects to corresponding code to make a change to the application
# Serializers (converts python into) -> Json data = to communicate with our web applications

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        #serialize to accept/return users
        model = User
        fields = [
            "id",
            "username",
            "password",
        ]
        #accept password when creating new user but dont return the password when we are giving information about the user
        #no one can read what the password is 
        extra_kwargs = {
            "password" : {"write_only": True}
        }
    #implemented a method to create user
    #serializer will check through Meta:model->fields to see if its valid 
    #validated_date = passes valid "username" & "password"
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "author"
        ]
        extra_kwargs = {
            "author": {"read_only": True} 
        }