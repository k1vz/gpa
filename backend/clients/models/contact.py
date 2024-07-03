from django.db import models
from .client import Client

class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	phone = models.CharField(max_length=50)
	phone_alt = models.CharField(max_length=50, blank=True, null=True)
	role = models.CharField(max_length=50, blank=True, null=True)

	client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contact')

	def __str__(self):
		return self.name
	