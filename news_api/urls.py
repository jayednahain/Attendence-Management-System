
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    path('scarpnews/',views.scarp_news, name="scarp_news_link")
]
