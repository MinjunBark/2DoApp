from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100) #title
    content = models.TextField() #content
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add -> automatically populate whenever we make an instance of this node
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes") #who made this node(FK) can link with user to collect user's data (One2Many) relationship
    
    
    def __str__(self):
        return self.title
    