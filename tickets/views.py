from django.urls import reverse
from django.views import View
from rest_framework import status
from .models.ticket import Ticket
from rest_framework.views import APIView
from .models.ticket_type import TicketType
from rest_framework.response import Response
from .forms import TicketForm, TicketTypeForm
from django.shortcuts import get_object_or_404, redirect, render
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

class TicketDetailView(View):
	def get(self, req, pk):
		try:
			ticket = Ticket.objects.get(pk=pk)
		except Ticket.DoesNotExist:
			raise NotFound('Ticket not found')

		return render(req, 'detail/detail_ticket.html', {'ticket': ticket})

class TicketUpdateView(View):
	def get(self, req, pk):
		ticket = get_object_or_404(Ticket, pk=pk)
		form = TicketForm(instance=ticket)

		return render(req, 'update/update_ticket.html', {
			'form': form,
			'ticket': ticket
		})

	def post(self, req, pk):
		ticket = get_object_or_404(Ticket, pk=pk)
		form = TicketForm(req.POST, instance=ticket)

		if form.is_valid():
			form.save()
			return redirect('ticket-detail', pk=pk)
		else:
			return render(req, 'update/update_ticket.html', {
				'form': form,
				'ticket': ticket
			})

class TicketDeleteView(APIView):
	def get(self, req, pk):
		try:
			ticket = Ticket.objects.get(pk=pk)
		except Ticket.DoesNotExist:
			raise NotFound('Ticket not found!')

		ticket.delete()
		return redirect(reverse('ticket-list'))

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

class TicketTypeUpdateView(View):
	def get(self, req, pk):
		ticket_type = get_object_or_404(TicketType, pk=pk)
		form = TicketTypeForm(instance=ticket_type)

		return render(req, 'update/update_ticket_type.html', {
			'form': form,
			'ticket_type': ticket_type
		})

	def post(self, req, pk):
		ticket_type = get_object_or_404(TicketType, pk=pk)
		form = TicketTypeForm(req.POST, instance=ticket_type)

		if form.is_valid():
			form.save()
			return redirect('ticket-type-detail', pk=pk)
		else:
			return render(req, 'update/update_ticket_type.html', {
				'form': form,
				'ticket_type': ticket_type
			})

class TicketTypeDeleteView(APIView):
	def get(self, req, pk):
		try:
			ticket_type = TicketType.objects.get(pk=pk)
		except TicketType.DoesNotExist:
			raise NotFound('Ticket type not found!')

		ticket_type.delete()
		return redirect(reverse('ticket-type-list'))
