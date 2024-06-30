from django.db import models
from clients.models.client import Client

class Driver(models.Model):
	active = models.BooleanField(default=True)
	name = models.CharField(max_length=100)
	cpf = models.CharField(max_length=14, unique=True)
	birth_date = models.DateField()
	license_type = models.CharField(max_length=2)
	cnh = models.CharField(max_length=11, unique=True)
	demerit_points = models.IntegerField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='drivers')

	def __str__(self):
		return self.name
