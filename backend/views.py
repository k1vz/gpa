from django.shortcuts import render
from rest_framework.views import APIView
from django.utils import timezone

from clients.models.client import Client
from drivers.models.driver import Driver
from drivers.models.daily import Daily
from tickets.models.ticket import Ticket

class HomeView(APIView):
	def get(self, req):
		month = timezone.now().month

		clients = Client.objects.count()
		active_clients = Client.objects.filter(active=True).count()
		drivers = Driver.objects.count()
		active_drivers = Driver.objects.filter(active=True).count()
		dailies = Daily.objects.count()
		last_month_dailies = Daily.objects.filter(date__month=month).count()
		tickets = Ticket.objects.count()
		last_month_tickets = Ticket.objects.filter(created_at__month=month).count()
		active_tickets = Ticket.objects.filter(active=True).count()

		context = {
			'clients': clients,
			'active_clients': active_clients,
			'drivers': drivers,
			'active_drivers': active_drivers,
			'inactive_drivers': drivers - active_drivers,
			'dailies': dailies,
			'last_month_dailies': last_month_dailies,
			'tickets': tickets,
			'last_month_tickets': last_month_tickets,
			'active_tickets': active_tickets
		}
		return render(req, 'home.html', context)
