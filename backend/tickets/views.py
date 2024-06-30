from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import TicketSerializer, TicketTypeSerializer
from .models.ticket_type import TicketType
from .models.ticket import Ticket

class TicketCreateView(APIView):
	def post(self, req):
		serializer = TicketSerializer(data=req.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class TicketDetailView(APIView):
	def get(self, req, pk):
		ticket = self.get_object(pk)
		serializer = TicketSerializer(ticket)

		return Response(serializer.data)

	def get_object(self, pk):
		try:
			return Ticket.objects.get(pk=pk, active=True)
		except Ticket.DoesNotExist:
			raise NotFound('Multa não encontrada')

class TicketListView(APIView):
	def get(self, req):
		tickets = Ticket.objects.filter(active=True)
		serializer = TicketSerializer(tickets, many=True)

		return Response(serializer.data)

class TicketUpdateView(APIView):
	def put(self, req, pk):
		ticket = self.get_object(pk)

		serializer = TicketSerializer(ticket, data=req.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data)

	def get_object(self, pk):
		try:
			return Ticket.objects.get(pk=pk, active=True)
		except Ticket.DoesNotExist:
			raise NotFound('Ticket not found')

class TicketDeleteView(APIView):
	def delete(self, req, pk):
		ticket = self.get_object(pk)
		ticket.active = False
		ticket.save()

		return Response({'message': 'Multa desativada com sucesso'}, status=status.HTTP_204_NO_CONTENT)

	def get_object(self, pk):
		try:
			return Ticket.objects.get(pk=pk, active=True)
		except Ticket.DoesNotExist:
			raise NotFound('Multa não encontrada')

class TicketTypeCreateView(APIView):
	def post(self, req):
		serializer = TicketTypeSerializer(data=req.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

class TicketTypeDetailView(APIView):
	def get(self, req, pk):
		ticket_type = self.get_object(pk)
		serializer = TicketTypeSerializer(ticket_type)

		return Response(serializer.data)

	def get_object(self, pk):
		try:
			return TicketType.objects.get(pk=pk)
		except TicketType.DoesNotExist:
			raise NotFound('Tipo de multa não encontrado')

class TicketTypeListView(APIView):
	def get(self, req):
		ticket_types = TicketType.objects.all()
		serializer = TicketTypeSerializer(ticket_types, many=True)
		return Response(serializer.data)

class TicketTypeUpdateView(APIView):
	def put(self, req, pk):
		ticket_type = self.get_object(pk)

		serializer = TicketTypeSerializer(ticket_type, data=req.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data)

	def get_object(self, pk):
		try:
			return TicketType.objects.get(pk=pk)
		except TicketType.DoesNotExist:
			raise NotFound('Tipo de multa não encontrado')

class TicketTypeDeleteView(APIView):
	def delete(self, req, pk):
		ticket_type = self.get_object(pk)
		ticket_type.delete()

		return Response({'message': 'Tipo de multa desativada com sucesso'}, status=status.HTTP_204_NO_CONTENT)

	def get_object(self, pk):
		try:
			return TicketType.objects.get(pk=pk)
		except TicketType.DoesNotExist:
			raise NotFound('Tipo de multa não encontrado')
