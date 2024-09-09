from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Rooms(models.Model):
    room_name=models.CharField(max_length=20)
    slug=models.SlugField(unique=True,null=True)
    def __str__(self):
        return str(self.room_name)
    
class Messages(models.Model):
    messages=models.TextField(max_length=20)
    room=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    sender=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.sender} from {self.room.room_name}'