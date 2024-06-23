# forms.py
from django import forms
from .models import Cliente
from .models import Motorista
from .models import Multa

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' 

class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['nome', 'cpf', 'data_nascimento', 'cnh', 'tipo_habilitacao', 'foto_cnh', 'foto_perfil']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class MultaForm(forms.ModelForm):
    class Meta:
        model = Multa
        fields = '__all__' 