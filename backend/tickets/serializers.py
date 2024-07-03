from rest_framework import serializers
from clients.serializers import ClientSerializer
from .models.ticket_type import TicketType
from .models.ticket import Ticket

class TicketTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = TicketType
		fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
	ticket_type = TicketTypeSerializer()
	client = ClientSerializer()

	class Meta:
		model = Ticket
		fields = '__all__'
