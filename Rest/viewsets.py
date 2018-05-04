from rest_framework import generics
from rest_framework import viewsets

from .serializers import AlertSerializer
from users.models import alert

class AlertViewSet(viewsets.ModelViewSet):
	queryset = alert.objects.all()
	serializer_class = AlertSerializer
