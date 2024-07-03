from .driver import Driver
from django.db import models

class WorkPeriod(models.Model):
	# ID da jornada é único em todo o banco de dados
	responsibleSignature = models.BooleanField(default=False)
	periodStart = models.DateTimeField()
	periodEnd = models.DateTimeField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='work_periods')

	def __str__(self):
		return f"Work Period #{self.id}"