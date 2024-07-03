from .work_period import WorkPeriod
from django.db import models

class Daily(models.Model):
	# ID da diária é único em todo o banco de dados
	date = models.DateField()
	start = models.DateTimeField()
	end = models.DateTimeField()
	intervalStart = models.DateTimeField()
	intervalEnd = models.DateTimeField()
	restStart = models.DateTimeField()
	restEnd = models.DateTimeField()
	employeeSignature = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	work_period = models.ForeignKey(WorkPeriod, on_delete=models.CASCADE, related_name='dailies')

	def __str__(self):
		return f"Daily Record #{self.id}"