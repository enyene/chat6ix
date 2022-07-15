from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

user_model = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(user_model,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username

class Friend(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE,related_name='friends')

    def __str__(self) -> str:
        return self.profile.user.username

class ChatMessage(models.Model):
    body = models.TextField()
    # msg_sender = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
    # msg_reciever = models.ForeignKey(Friend,on_delete=models.CASCADE,related_name='receiver')
    msg_sender = models.CharField(max_length=12)
    msg_reciever = models.CharField(max_length=12)
    seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.body[:50]
