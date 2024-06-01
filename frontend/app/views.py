from django.shortcuts import render
# Importe a função gerar_dados_ficticios de utils.py
from .utils import gerar_dados_ficticios

def base(request):
    return render(request, 'base.html')

def clientes(request):
    return render(request, 'clientes.html')

def lista_clientes(request):
    # Dados fictícios dos clientes para testes
    clientes = [
        {'nome': 'Cliente A', 'cnpj': '123456789', 'tipo_empresa': 'Tipo 1', 'ativa': True},
        {'nome': 'Cliente B', 'cnpj': '987654321', 'tipo_empresa': 'Tipo 2', 'ativa': False},
        # Adicione mais clientes fictícios conforme necessário
    ]
    # Renderize o template com os dados dos clientes
    return render(request, 'clientes.html', {'clientes': clientes})

def motoristas(request):
    return render(request, 'motoristas.html')

def multas(request):
    return render(request, 'multas.html')

def jornadas(request):
    return render(request, 'jornadas.html')





