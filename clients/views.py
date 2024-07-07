from django.views import View
from django.urls import reverse
from .models.client import Client
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.exceptions import NotFound
from .forms import ClientForm, AddressForm, ContactForm
from .serializers import ClientSerializer, ClientListSerializer

class ClientCreateView(View):
	def get(self, req):
		client_form = ClientForm()
		address_form = AddressForm()
		contact_form = ContactForm()

		return render(req, 'create/create_client.html', {
			'client_form': client_form,
			'address_form': address_form,
			'contact_form': contact_form
		})

	def post(self, req):
		client_form = ClientForm(req.POST)
		address_form = AddressForm(req.POST)
		contact_form = ContactForm(req.POST)

		if client_form.is_valid() and address_form.is_valid() and contact_form.is_valid():
			address = address_form.save()
			contact = contact_form.save()

			client = client_form.save(commit=False)
			client.address = address
			client.contact = contact

			client.save()
		else:
			print(client_form.errors)
			print(address_form.errors)
			print(contact_form.errors)

		return redirect('home')

class ClientDetailView(APIView):
	def get(self, req, pk):
		client = Client.objects.get(pk=pk)
		serializer = ClientSerializer(client)

		return render(req, 'detail/detail_client.html', {'client': serializer.data})

# class ClientDetailAPIView(APIView):
# 	def get(self, req, pk):
# 		client = self.get_object(pk)
# 		serializer = ClientSerializer(client)

# 		return Response(serializer.data)

class ClientListView(APIView):
	def get(self, req):
		clients = Client.objects.all()
		serializer = ClientListSerializer(clients, many=True)

		return render(req, 'view/view_clients.html', {'clients': serializer.data})

class ClientUpdateView(View):
	def get(self, request, pk):
		client = get_object_or_404(Client, pk=pk)
		client_form = ClientForm(instance=client)
		address_form = AddressForm(instance=client.address)
		contact_form = ContactForm(instance=client.contact)

		return render(request, 'update/update_client.html', {
			'client_form': client_form,
			'address_form': address_form,
			'contact_form': contact_form,
			'client': client
		})

	def post(self, request, pk):
		client = get_object_or_404(Client, pk=pk)
		client_form = ClientForm(request.POST, instance=client)
		address_form = AddressForm(request.POST, instance=client.address)
		contact_form = ContactForm(request.POST, instance=client.contact)

		if client_form.is_valid() and address_form.is_valid() and contact_form.is_valid():
			client_form.save()
			address_form.save()
			contact_form.save()
			return redirect('client-detail', pk=client.pk)
		else:
			return render(request, 'update/update_client.html', {
				'client_form': client_form,
				'address_form': address_form,
				'contact_form': contact_form,
				'client': client,
				'errors': {
					'client_form_errors': client_form.errors,
					'address_form_errors': address_form.errors,
					'contact_form_errors': contact_form.errors
				}
			})

# class ClientUpdateAPIView(APIView):
# 	def put(self, req, pk):
# 		try:
# 			client = Client.objects.get(pk=pk)
# 		except Client.DoesNotExist:
# 			raise NotFound('Client not found!')

# 		serializer = ClientSerializer(client, data=req.data)

# 		if serializer.is_valid():
# 			serializer.save()

# 			return Response(serializer.data)

# 		return Response(serializer.errors, status=status.HTTP_400_BAD_req)

class ClientDeleteView(APIView):
	def get(self, req, pk):
		try:
			client = Client.objects.get(pk=pk)
		except Client.DoesNotExist:
			raise NotFound('Client not found!')

		client.active = False
		client.save()
		return redirect(reverse('client-list'))
