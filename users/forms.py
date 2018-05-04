from django import forms
from .models import profile

class profile_form(forms.ModelForm):
    class Meta:        
        model = profile
        fields = (
            'name',
            'address',
            'telephone',
            'picture',
        )

        labels = {
            'name': 'Nombre',
            'address': 'Direccion',
            'telephone': 'Telefono',
            'picture': 'Foto',
        }