from django import forms
from .models.client import Client
from .models.address import Address
from .models.contact import Contact

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'street', 'number', 'city', 'state', 'reference_point', 'neighborhood', 'complement'
        ]
        labels = {
            'street': 'Rua',
            'number': 'Número',
            'city': 'Cidade',
            'state': 'Estado',
            'reference_point': 'Ponto de Referência',
            'neighborhood': 'Bairro',
            'complement': 'Complemento'
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'email', 'phone', 'phone_alt', 'role'
        ]
        labels = {
            'email': 'E-mail',
            'phone': 'Telefone',
            'phone_alt': 'Telefone Alternativo',
            'role': 'Cargo'
        }

class ClientForm(forms.ModelForm):
    birth_date = forms.DateField(
        label='Data de Nascimento',
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
     
    class Meta:
        model = Client
        fields = [
            'client_type', 'name', 'active', 'defaulting', 'cpf', 'cnpj', 'birth_date', 'truck_count', 'business_registration', 'trade_name'
        ]
        labels = {
            'client_type': 'Tipo de Cliente',
            'name': 'Nome',
            'active': 'Ativo',
            'defaulting': 'Inadimplente',
            'cpf': 'CPF',
            'cnpj': 'CNPJ',
            'truck_count': 'Quantidade de Caminhões',
            'business_registration': 'Inscrição Estadual',
            'trade_name': 'Nome Fantasia',
        }
