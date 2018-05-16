from django.contrib import admin
from django.urls import path
from .views import main_page, create_profile, profile_list, LoginView, alerts_list, bomberos_list, logout_user
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout

urlpatterns = [
    path('', main_page),
    path('main', main_page, name = 'main'),
    path('create_profile', create_profile, name = 'create_profile'),
    path('profile_list', profile_list, name = 'profile_list'),
    path('bomberos_list', bomberos_list, name = 'bomberos_list'),
    path('login', LoginView.as_view(), name = 'login'),
    path('logout', logout_user, name = 'logout'),
    path('alert', alerts_list, name = 'alert'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)