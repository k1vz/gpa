from django.views import View
from .models.client import Client
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.exceptions import NotFound
from .forms import ClientForm, AddressForm, ContactForm
from .serializers import ClientSerializer, ClientListSerializer

class ClientCreateView(View):
	def get(self, req):
		client_form = ClientForm()
		address_form = AddressForm()
		contact_form = ContactForm()

		return render(req, 'cadastrar_cliente.html', {
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
		client = self.get_object(pk)
		serializer = ClientSerializer(client)

		return Response(serializer.data)

class ClientListView(APIView):
	def get(self, req):
		clients = Client.objects.all()
		serializer = ClientListSerializer(clients, many=True)
		
		# return Response(serializer.data)
		return render(req, 'clientes.html', {'clients': serializer.data})

class ClientUpdateView(APIView):
	def put(self, req, pk):
		try:
			client = Client.objects.get(pk=pk)
		except Client.DoesNotExist:
			raise NotFound('Client not found!')

		serializer = ClientSerializer(client, data=req.data)
		
		if serializer.is_valid():
			serializer.save()
			
			return Response(serializer.data)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_req)

class ClientDeleteView(APIView):
	def delete(self, req, pk):
		try:
			client = Client.objects.get(pk=pk)
		except Client.DoesNotExist:
			raise NotFound('Client not found!')

		client.delete()
		return Response({'message': 'Client deleted successfully'}, status=status.HTTP_204_NO_CONTENT)