from rest_framework import serializers
from .models.client import Client
from .models.address import Address
from .models.contact import Contact

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
	address = AddressSerializer()
	contact = ContactSerializer()

	class Meta:
		model = Client
		fields = '__all__'

	def create(self, validated_data):
		address_data = validated_data.pop('address')
		contact_data = validated_data.pop('contact')

		address = Address.objects.create(**address_data)
		contact = Contact.objects.create(**contact_data)

		client = Client.objects.create(
			address=address,
			contact=contact,
			**validated_data
		)

		if client.client_type == 'PJ':
			client.cpf = None
		elif client.client_type == 'PF':
			client.cnpj = None
		client.save()

		return client

	def update(self, instance, validated_data):
		address_data = validated_data.pop('address', None)
		contact_data = validated_data.pop('contact', None)

		if address_data:
			Address.objects.filter(id=instance.address.id).update(**address_data)

		if contact_data:
			Contact.objects.filter(id=instance.contact.id).update(**contact_data)

		for attr, value in validated_data.items():
			setattr(instance, attr, value)

		if instance.client_type == 'PJ':
			instance.cpf = None
		elif instance.client_type == 'PF':
			instance.cnpj = None

		instance.save()
		return instance

class ClientListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = ['id', 'name', 'client_type', 'active']

	def to_representation(self, instance):
		representation = super().to_representation(instance)

		if instance.client_type == 'PJ':
			representation['cnpj'] = instance.cnpj
		elif instance.client_type == 'PF':
			representation['cpf'] = instance.cpf

		return representation
