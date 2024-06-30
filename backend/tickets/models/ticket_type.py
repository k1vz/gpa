from django.db import models

class TicketType(models.Model):
	code = models.IntegerField()
	description = models.CharField(max_length=100)
	legal_basis = models.CharField(max_length=50)
	classification = models.CharField(max_length=50)

	def __str__(self):
		return self.description
