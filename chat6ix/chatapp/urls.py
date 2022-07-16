from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('details/',views.detail,name='detail'),
    path('sent/<str:pk>/',views.sentMessages,name='sent'),
    path('register/',views.register,name='register')

]