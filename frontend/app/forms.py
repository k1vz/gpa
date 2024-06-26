# forms.py
from django import forms
from .models import Cliente, Jornada, Motorista, Multa, Frota

class ClienteForm(forms.Form):
    # Tópico: Informações Gerais
    tipo_pessoa = forms.CharField(label='Tipo Pessoa', max_length=100)
    cnpj = forms.CharField(label='CNPJ', max_length=18)
    razao_social = forms.CharField(label='Razão Social', max_length=255)
    nome_fantasia = forms.CharField(label='Nome Fantasia', max_length=255)
    tipo_empresa = forms.CharField(label='Tipo Empresa', max_length=100)
    quantidade_caminhoes = forms.IntegerField(label='Quantidade Caminhões')

    # Tópico: Contato
    nome = forms.CharField(label='Nome', max_length=100)
    cargo = forms.CharField(label='Cargo', max_length=100)
    email = forms.EmailField(label='Email')
    telefone_primario = forms.CharField(label='Telefone Primário', max_length=20)
    telefone_secundario = forms.CharField(label='Telefone Secundário', max_length=20)

    # Tópico: Endereço
    logradouro = forms.CharField(label='Logradouro', max_length=255)
    numero = forms.CharField(label='Número', max_length=10)
    municipio = forms.CharField(label='Município', max_length=100)
    estado = forms.CharField(label='Estado', max_length=50)
    bairro = forms.CharField(label='Bairro', max_length=100)
    complemento = forms.CharField(label='Complemento', max_length=255)
    ponto_referencia = forms.CharField(label='Ponto de Referência', max_length=255)

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