from django.views import View
from rest_framework import status
from .models.ticket import Ticket
from rest_framework.views import APIView
from .models.ticket_type import TicketType
from rest_framework.response import Response
from .forms import TicketForm, TicketTypeForm
from django.shortcuts import redirect, render
from rest_framework.exceptions import NotFound
from .serializers import TicketSerializer, TicketTypeSerializer

class TicketCreateView(View):
	def get(self, req):
		ticket_form = TicketForm()

		return render(req, 'create/create_ticket.html', {
			'form': ticket_form,
		})
	
	def post(self, req):
		ticket_form = TicketForm(req.POST)

		if ticket_form.is_valid():
			ticket = ticket_form.save(commit=False)

			ticket.save()
		else:
			print(ticket_form.errors)

		return redirect('ticket-list')

# class TicketCreateAPIView(APIView):
# 	def post(self, req):
# 		serializer = TicketSerializer(data=req.data)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()
		
# 		return Response(serializer.data, status=status.HTTP_201_CREATED)

class TicketDetailView(APIView):
	def get(self, req, pk):
		ticket = self.get_object(pk)
		serializer = TicketSerializer(ticket)

		return Response(serializer.data)

	def get_object(self, pk):
		try:
			return Ticket.objects.get(pk=pk, active=True)
		except Ticket.DoesNotExist:
			raise NotFound('Ticket not found')


class TicketListView(APIView):
	def get(self, req):
		tickets = Ticket.objects.all()
		serializer = TicketSerializer(tickets, many=True)

		return render(req, 'view/view_tickets.html', {'tickets': serializer.data})

# class TicketListAPIView(APIView):
# 	def get(self, req):
# 		tickets = Ticket.objects.filter(active=True)
# 		serializer = TicketSerializer(tickets, many=True)

# 		return Response(serializer.data)

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

		return Response({'message': 'Ticket deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

	def get_object(self, pk):
		try:
			return Ticket.objects.get(pk=pk, active=True)
		except Ticket.DoesNotExist:
			raise NotFound('Ticket not found')
		
		

class TicketTypeCreateView(View):
	def get(self, req):
		ticket_type_form = TicketTypeForm()

		return render(req, 'create/create_ticket_type.html', {
			'form': ticket_type_form,
		})
	
	def post(self, req):
		ticket_type_form = TicketTypeForm(req.POST)

		if ticket_type_form.is_valid():
			ticket_type = ticket_type_form.save(commit=False)

			ticket_type.save()
			return redirect('ticket-type-list')
		else:
			print(ticket_type_form.errors)
			return render(req, 'create/create_ticket_type.html', {'form': ticket_type_form})

# class TicketTypeCreateAPIView(APIView):
# 	def post(self, req):
# 		serializer = TicketTypeSerializer(data=req.data)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()

# 		return Response(serializer.data, status=status.HTTP_201_CREATED)

class TicketTypeDetailView(APIView):
	def get(self, req, pk):
		ticket_type = self.get_object(pk)
		serializer = TicketTypeSerializer(ticket_type)

		return Response(serializer.data)

	def get_object(self, pk):
		try:
			return TicketType.objects.get(pk=pk)
		except TicketType.DoesNotExist:
			raise NotFound('Ticket type not found')

class TicketTypeListView(APIView):
	def get(self, req):
		ticket_types = TicketType.objects.all()
		serializer = TicketTypeSerializer(ticket_types, many=True)

		return render(req, 'view/view_ticket_types.html', {'ticket_types': serializer.data})

# class TicketTypeListAPIView(APIView):
# 	def get(self, req):
# 		ticket_types = TicketType.objects.all()
# 		serializer = TicketTypeSerializer(ticket_types, many=True)
# 		return Response(serializer.data)

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
			raise NotFound('Ticket type not found')

class TicketTypeDeleteView(APIView):
	def delete(self, req, pk):
		ticket_type = self.get_object(pk)
		ticket_type.delete()

		return Response({'message': 'Ticket type deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

	def get_object(self, pk):
		try:
			return TicketType.objects.get(pk=pk)
		except TicketType.DoesNotExist:
			raise NotFound('Ticket type not found')
