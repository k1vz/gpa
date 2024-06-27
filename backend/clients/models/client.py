from django.db import models
from .address import Address
from .contact import Contact

class Client(models.Model):
	CLIENT_TYPE = [
		('PJ', 'Legal Entity'),
		('PF', 'Natural Person'),
	]

	active = models.BooleanField(default=True)
	name = models.CharField(max_length=255)
	defaulting = models.BooleanField(default=False)
	client_type = models.CharField(max_length=2, choices=CLIENT_TYPE)
	cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
	cnpj = models.CharField(max_length=18, unique=True, blank=True, null=True)
	birth_date = models.DateField(blank=True, null=True)
	business_registration = models.CharField(max_length=9, blank=True, null=True)
	address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='clients')
	truck_count = models.IntegerField()
	corporate_name = models.CharField(max_length=100, blank=True, null=True)
	trade_name = models.CharField(max_length=100, blank=True, null=True)
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='clients')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.client_type == 'PJ':
			self.cpf = None
			self.birth_date = None
		elif self.client_type == 'PF':
			self.cnpj = None
			self.business_registration = None
			self.corporate_name = None
			self.trade_name = None
		super(Client, self).save(*args, **kwargs)
