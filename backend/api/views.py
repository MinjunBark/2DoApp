from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
# creating a new user (registration)
# inherit from generics that automatically handles creating new user or objects
class CreateUserView(generics.CreateAPIView):
    # making sure we dont create a user that already exist
    queryset = User.objects.all()
    #tells the view what kind of data to accept to make a new user
    serializer_class = UserSerializer
    #who can actually call this(i.e.. "Anyone")
    permission_classes = [AllowAny]
    
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    # custom functionality (override)
    # manually checking passing data
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)