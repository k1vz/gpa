from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import ClienteSerializer
from .models.cliente import Cliente

class ClienteCreateView(APIView):
	def post(self, req):
		serializer = ClienteSerializer(data=req.data)

		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

class ClienteDetailView(APIView):
	def get(self, req, pk):
		cliente = self.get_object(pk)
		serializer = ClienteSerializer(cliente)

		return Response(serializer.data)

	def put(self, req, pk):
		cliente = self.get_object(pk)

		serializer = ClienteSerializer(cliente, data=req.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data)

	def patch(self, req, pk):
		cliente = self.get_object(pk)

		serializer = ClienteSerializer(cliente, data=req.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data)

	def delete(self, req, pk):
		cliente = self.get_object(pk)
		cliente.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

class ClienteListView(APIView):
	def get(self, req):
		clientes = Cliente.objects.all()
		serializer = ClienteSerializer(clientes, many=True)

		return Response(serializer.data)

