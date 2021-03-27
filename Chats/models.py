from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    name = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    chats = models.ManyToManyField(Chat)

class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    pub_date = models.DateTimeField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

