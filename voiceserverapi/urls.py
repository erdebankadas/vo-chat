from django.contrib import admin
from django.urls import path,include
from . import views
from voiceserverapi.views import *

urlpatterns = [
    path('voiceapi/',views.server)
]
