from .forms import ClientForm
from django.views import View
from .models.client import Client
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.exceptions import NotFound
from .serializers import ClientSerializer, ClientListSerializer

class ClientCreateView(View):
	def get(self, req):
		client_form = ClientForm()

		return render(req, 'cadastrar_cliente.html', {'form': client_form})

	def post(self, req):
		form = ClientForm(req.POST)
		if form.is_valid():
			form.save()
			client = form.save(commit=False)
			client.save()

			serializer = ClientSerializer(data=req.data)

			serializer.is_valid(raise_exception=True)
			serializer.save()

			return redirect('home')
		else:
			form = ClientForm()

		return render(req, 'cadastrar_cliente.html', {'form': form})


# class ClientCreateView(APIView):
# 	def post(self, req):
# 		serializer = ClientSerializer(data=req.data)

# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()

# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	
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