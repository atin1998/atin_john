from django.urls import path
from rest_framework import routers
from practicedemo import views

urlpatterns = [
    ('members_atin_api/',views.SelectionMember.as_view())
]
