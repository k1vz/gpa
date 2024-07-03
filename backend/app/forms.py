# forms.py
from django import forms
from .models import Jornada, Motorista, Multa, Frota

class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['nome', 'cpf', 'data_nascimento', 'cnh', 'tipo_habilitacao', 'foto_cnh']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class MultaForm(forms.ModelForm):
    class Meta:
        model = Multa
        fields = '__all__'

class JornadaForm(forms.ModelForm):
    class Meta:
        model = Jornada
        fields = '__all__'

class FrotaForm(forms.ModelForm):
    class Meta:
        model = Frota
        fields = ['placa', 'cor', 'motorista', 'modelo', 'ano']