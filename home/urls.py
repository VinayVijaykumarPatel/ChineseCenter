import os
from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path("home",views.index,name='home'),
     path("about",views.about,name='about'),
      path("services",views.services,name='services'),
      path("services1",views.services1,name='services1'),
      path("services2",views.services2,name='services2'),
      path("contact",views.contact,name='contact')
]