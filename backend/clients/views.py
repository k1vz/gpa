from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import ClientSerializer
from .models.client import Client

class ClientCreateView(APIView):
	def post(self, req):
		serializer = ClientSerializer(data=req.data)

		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

class ClientDetailView(APIView):
	def get(self, req, pk):
		client = self.get_object(pk)
		serializer = ClientSerializer(client)

		return Response(serializer.data)

class ClientListView(APIView):
	def get(self, req):
		clients = Client.objects.all()
		serializer = ClientSerializer(clients, many=True)

		return Response(serializer.data)

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
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDeleteView(APIView):
    def delete(self, req, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise NotFound('Client not found!')

        client.delete()
        return Response({'message': 'Client deleted successfully'}, status=status.HTTP_204_NO_CONTENT)