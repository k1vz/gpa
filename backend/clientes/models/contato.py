from django.db import models

class Contato(models.Model):
	nome = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	telefone = models.CharField(max_length=50)
	telefone_secundario = models.CharField(max_length=50, blank=True, null=True)
	cargo = models.CharField(max_length=50, blank=True, null=True)
	cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE, related_name='contatos')

	def __str__(self):
		return self.nome
	