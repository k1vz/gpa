from django import forms
from .models.ticket import Ticket
from .models.ticket_type import TicketType
from clients.models.client import Client

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        labels = {
            'due_date': 'Data de Vencimento',
            'infraction_datetime': 'Data da Infração',
            'city': 'Cidade',
            'state': 'Estado',
            'infraction_location': 'Local da Infração',
            'ait': 'Auto de Infração de Trânsito',
            'denatran_agency_code': 'Código do Órgão Denatran',
            'autuador_agency_code': 'Código do Autuador',
            'observation': 'Observações',
            'active': 'Ativo',
            'judicial_status': 'Status Judicial',
            'license_plate': 'Placa do Veículo',
            'client': 'Cliente',
            'ticket_type': 'Tipo de Multa',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['due_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['infraction_datetime'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['ticket_type'].queryset = TicketType.objects.all()
        self.fields['client'].queryset = Client.objects.all()

class TicketTypeForm(forms.ModelForm):
    class Meta:
        model = TicketType
        fields = '__all__'
        labels = {
            'code': 'Código',
            'description': 'Descrição',
            'legal_basis': 'Fundamento Legal',
            'classification': 'Classificação',
        }
