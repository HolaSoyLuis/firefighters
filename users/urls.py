from django.contrib import admin
from django.urls import path
from .views import main_page, new_profile, c_profile

urlpatterns = [
    path('', main_page),
    path('main', main_page, name = 'main'),
    path('new_profile', new_profile, name = 'new_profile'),
    path('create_profile', new_profile, name = 'create_profile'),    
]
