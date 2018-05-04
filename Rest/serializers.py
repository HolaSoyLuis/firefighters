from rest_framework import serializers

from users.models import alert

class AlertSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = alert
		fields = ('name', 'DPI', 'telephone', 'coord','address', 'alerts')
