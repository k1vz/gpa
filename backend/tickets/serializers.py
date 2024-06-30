from rest_framework import serializers
from .models.ticket_type import TicketType
from .models.ticket import Ticket

class TicketTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = TicketType
		fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = '__all__'
