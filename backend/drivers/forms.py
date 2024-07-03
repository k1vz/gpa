from django import forms
from .models.driver import Driver
from clients.models.client import Client

class DriverForm(forms.ModelForm):
    birth_date = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = Driver
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'cpf': 'CPF',
            'birth_date': 'Data de Nascimento',
            'license_type': 'Tipo da CNH',
            'cnh': 'CNH',
            'demerit_points': 'Pontos na CNH',
            'client': 'Cliente Associado'
        }
        widgets = {
            'license_type': forms.Select(choices=Driver.LICENSE_TYPE)
        }
