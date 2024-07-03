from django.db import models

class Address(models.Model):
	street = models.CharField(max_length=255)
	number = models.IntegerField()
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=2)
	reference_point = models.CharField(max_length=255, blank=True, null=True)
	neighborhood = models.CharField(max_length=100)
	complement = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f"{self.street}, {self.number} - {self.city}/{self.city}"
