from django.contrib import admin
from django.urls import path
from .views import main_page, create_profile, profile_list, LoginView, alerts_list, bomberos_list, logout_user,ReportePersonasPDF
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout
from .views import es_atendido
from .views import alerts_list_fire, alerts_list_transit, alerts_list_maternity, alerts_list_first_aid

urlpatterns = [
    path('', main_page),
    path('main', main_page, name = 'main'),
    path('create_profile', create_profile, name = 'create_profile'),
    path('profile_list', profile_list, name = 'profile_list'),
    path('bomberos_list', bomberos_list, name = 'bomberos_list'),
    path('login', LoginView.as_view(), name = 'login'),
    path('logout', logout_user, name = 'logout'),
    path('alert', alerts_list, name = 'alert'),
    path('reporte_personas_pdf', ReportePersonasPDF.as_view(), name='reporte_personas_pdf'),
    path('atendido/<int:id>/', es_atendido.as_view(), name='atendido'),
    path('incendio', alerts_list_fire, name = 'incendio'),
    path('transito', alerts_list_transit, name = 'transito'),
    path('primeros_auxilios', alerts_list_first_aid, name = 'primeros_auxilios'),
    path('maternidad', alerts_list_maternity, name = 'maternidad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)