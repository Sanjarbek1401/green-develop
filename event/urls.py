

from django.contrib import admin
from django.urls import path, include

from event import views

urlpatterns = [
 path('', views.index, name="index"),
 path('registration', views.registration, name='registration'),
 path('about', views.about, name='about'),
 path('authors', views.authors, name='authors'),
 path('schedule', views.schedule, name='schedule'),
 path('venue', views.venue, name='venue'),
 path('registration', views.registration, name='registration'),
 ]