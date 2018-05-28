from rest_framework import serializers

from users.models import Persona

class AlertSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Persona
		fields = ('nombre', 'telefono', 'coordenadas','direccion', 'emergencia')
