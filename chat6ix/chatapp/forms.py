from pyexpat import model
from django import forms
from django.forms import ModelForm
from pikepdf import PasswordError
from .models import ChatMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
user = get_user_model()

@login_required
class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'forms','rows':3,'placeholder':'message......'}))
    class Meta:
        model = ChatMessage
        fields = ['body',]


class RegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    # password1 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = user
        fields = ()
        