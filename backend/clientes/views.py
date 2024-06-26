from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models.cliente import Cliente
from .serializers import ClienteSerializer

class ClienteCreateView(APIView):
	def post(self, request):
		serializer = ClienteSerializer(data=request.data)

		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

class ClienteDetailView(APIView):
	def get_object(self, pk):
		try:
			return Cliente.objects.get(pk=pk)
		except Cliente.DoesNotExist:
			raise NotFound('Cliente não encontrado')

	def get(self, request, pk):
		cliente = self.get_object(pk)
		serializer = ClienteSerializer(cliente)

		return Response(serializer.data)

	def put(self, request, pk):
		cliente = self.get_object(pk)

		serializer = ClienteSerializer(cliente, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data)

	def patch(self, request, pk):
		cliente = self.get_object(pk)

		serializer = ClienteSerializer(cliente, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data)

	def delete(self, request, pk):
		cliente = self.get_object(pk)
		cliente.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

class ClienteListView(APIView):
	def get(self, request):
		clientes = Cliente.objects.all()
		serializer = ClienteSerializer(clientes, many=True)

		return Response(serializer.data)

