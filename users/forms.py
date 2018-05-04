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
        labels = (
            {'Nombre': 'name'},
            {'Direccion': 'address'},
            {'Telefono': 'telephone'},
            {'Foto': 'picture'},
        )