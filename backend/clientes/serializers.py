from rest_framework import serializers
from .models.cliente import Cliente
from .models.endereco import Endereco
from .models.contato import Contato

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'estado']

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'telefone', 'email']

class ClienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    contato = ContatoSerializer()

    class Meta:
        model = Cliente
        fields = [
            'id', 'ativo', 'nome', 'inadimplente', 'tipo_cliente', 'cpf', 'cnpj', 'dataNascimento', 
            'inscricaoEstadual', 'endereco', 'qntCaminhoes', 'razaoSocial', 'nomeFantasia', 
            'contato', 'data_criacao', 'data_modificacao'
        ]

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        contato_data = validated_data.pop('contato')

        endereco = Endereco.objects.create(**endereco_data)
        contato = Contato.objects.create(**contato_data)

        cliente = Cliente.objects.create(
            endereco=endereco,
            contato=contato,
            **validated_data
        )
        
        if cliente.tipo_cliente == 'PJ':
            cliente.cpf = None
        elif cliente.tipo_cliente == 'PF':
            cliente.cnpj = None
        cliente.save()

        return cliente

    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        contato_data = validated_data.pop('contato', None)

        if endereco_data:
            Endereco.objects.filter(id=instance.endereco.id).update(**endereco_data)
        
        if contato_data:
            Contato.objects.filter(id=instance.contato.id).update(**contato_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if instance.tipo_cliente == 'PJ':
            instance.cpf = None
        elif instance.tipo_cliente == 'PF':
            instance.cnpj = None
        
        instance.save()
        return instance
