from django.db import models
from .ticket_type import TicketType
from clients.models.client import Client

class Ticket(models.Model):
	due_date = models.DateTimeField()
	infraction_datetime = models.DateTimeField()
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	infraction_location = models.CharField(max_length=50)
	ait = models.IntegerField(unique=True) # Auto de Infração de Trânsito
	denatran_agency_code = models.IntegerField()
	autuador_agency_code = models.IntegerField()
	observation = models.CharField(max_length=100, blank=True, null=True)
	active = models.BooleanField(default=True)
	judicial_status = models.CharField(max_length=50)
	license_plate = models.CharField(max_length=7)
	client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='tickets')
	ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name='tickets')

	def __str__(self):
		return f"Ticket {self.id} - {self.ticket_type.description}"
