from django.dispatch import receiver
from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.urls import reverse_lazy
from .models import ChatMessage, Profile,Friend
import json

from .forms import ChatMessageForm
# Create your views here.
def home(request):
    return HttpResponse('welcome to chat6ix')

'''
def index(request,pk):
    user = Profile.user
    friends = Friend.objects.get(profile_id=pk)
    context = {'user':user,'friends':friends}
    return render (request,'chatapp/index.html',context)

'''

def detail(request):
    friend = Friend.objects.get(id = 1)
    form = ChatMessageForm()
    sender = request.user
    receiver = Profile.objects.get(id = friend.profile.id)
    msg = ChatMessage.objects.all()
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.msg_sender = sender
            chat.msg_reciever = receiver
            chat.save()
            return  redirect (detail)
    context = {'form':form,'sender':sender,'reciever':receiver,'message':msg}
    return render (request,'chatapp/index.html',context)

def sentMessages(request,pk):
    data = json.loads(request.body)
    chat = data['msg']
    message = ChatMessage.objects.create(body=chat)
    return JsonResponse(message.body,safe=False)