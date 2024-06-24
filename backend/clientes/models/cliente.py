from django.db import models
from users.models import User
from .endereco import Endereco
from .contato import Contato

class Cliente(models.Model):
	TIPO_CLIENTE_CHOICES = [
		('PJ', 'Pessoa Jurídica'),
		('PF', 'Pessoa Física'),
	]

	ativo = models.BooleanField(default=True)
	nome = models.CharField(max_length=255)
	inadimplente = models.BooleanField(default=False)
	tipo_cliente = models.CharField(max_length=2, choices=TIPO_CLIENTE_CHOICES)
	cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
	cnpj = models.CharField(max_length=18, unique=True, blank=True, null=True)
	dataNascimento = models.DateField()
	inscricaoEstadual = models.CharField(max_length=9)
	endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name='clientes')
	qntCaminhoes = models.IntegerField()
	razaoSocial = models.CharField(max_length=100)
	nomeFantasia = models.CharField(max_length=100)
	contato = models.ForeignKey(Contato, on_delete=models.CASCADE, related_name='clientes')
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clientes')
	data_criacao = models.DateTimeField(auto_now_add=True)
	data_modificacao = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nome

	def save(self, *args, **kwargs):
		if self.tipo_cliente == 'PJ':
			self.cpf = None
		elif self.tipo_cliente == 'PF':
			self.cnpj = None
		super(Cliente, self).save(*args, **kwargs)
		