from cProfile import Profile
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register([models.Profile,models.ChatMessage,models.Friend])