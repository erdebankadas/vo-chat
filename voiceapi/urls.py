from django.contrib import admin
from django.urls import path,include
from voiceapi.views import * 
from . import views

urlpatterns = [
    path('',views.client)
]
