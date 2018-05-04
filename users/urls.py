from django.contrib import admin
from django.urls import path
from .views import main_page, create_profile, profile_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_page),
    path('main', main_page, name = 'main'),
    path('create_profile', create_profile, name = 'create_profile'),
    path('profile_list', profile_list, name = 'profile_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)