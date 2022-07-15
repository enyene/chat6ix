from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import ChatMessage


class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'forms','rows':3,'placeholder':'message......'}))
    class Meta:
        model = ChatMessage
        fields = ['body',]