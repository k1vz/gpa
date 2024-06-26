from django.db import models

class Endereco(models.Model):
	logradouro = models.CharField(max_length=255)
	numero = models.IntegerField()
	municipio = models.CharField(max_length=100)
	estado = models.CharField(max_length=2)
	ponto_referencia = models.CharField(max_length=255, blank=True, null=True)
	bairro = models.CharField(max_length=100)
	complemento = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f"{self.logradouro}, {self.numero} - {self.municipio}/{self.estado}"
	