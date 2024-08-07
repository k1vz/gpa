from django.db import models

class Contact(models.Model):
	email = models.EmailField(max_length=50, blank=True, null=True)
	phone = models.CharField(max_length=50)
	phone_alt = models.CharField(max_length=50, blank=True, null=True)
	role = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.name
	