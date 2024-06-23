# models.py
from django.db import models
class Cliente(models.Model):
    TIPO_PESSOA_CHOICES = [
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    ]
    
    tipo_pessoa = models.CharField(max_length=1, choices=TIPO_PESSOA_CHOICES)
    cnpj = models.CharField(max_length=18)
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    tipo_empresa = models.CharField(max_length=100)
    quantidade_caminhoes = models.IntegerField()
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    email = models.EmailField()
    telefone_primario = models.CharField(max_length=20)
    telefone_secundario = models.CharField(max_length=20, blank=True, null=True)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    ponto_referencia = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome  # Retorna o nome do cliente como representação no admin
    
class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    cnh = models.CharField(max_length=20)
    tipo_habilitacao = models.CharField(max_length=20)
    foto_cnh = models.ImageField(upload_to='motoristas/cnh/')
    foto_perfil = models.ImageField(upload_to='motoristas/perfil/')

    def __str__(self):
        return self.nome
    
class Multa(models.Model):
    multa_tipificada = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    motorista = models.CharField(max_length=100)
    placa_veiculo = models.CharField(max_length=20)
    vencimento = models.DateField()
    data_infracao = models.DateField()
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=200)
    codigo_denatran = models.CharField(max_length=20)
    codigo_atuador = models.CharField(max_length=20)
    estado_judicial = models.CharField(max_length=100)
    numero_auto_infracoes = models.CharField(max_length=20)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.multa_tipificada} - {self.cliente.nome} - {self.motorista.nome}"