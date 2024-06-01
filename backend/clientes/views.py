from rest_framework import viewsets
from .models.cliente import Cliente
from .models.endereco import Endereco
from .models.contato import Contato
from .serializers import ClienteSerializer, EnderecoSerializer, ContatoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
