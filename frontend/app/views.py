from django.shortcuts import render
# Importe a função gerar_dados_ficticios de utils.py
from .utils import gerar_dados_ficticios
from django.shortcuts import render, redirect
from .forms import ClienteForm
from .forms import MotoristaForm
from .forms import MultaForm

# --Base--
def base(request):
    return render(request, 'base.html')

# --Clientes--
def clientes(request):
    return render(request, 'clientes.html')

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return redirect('clientes')  # Redireciona para a página de listagem de clientes
    else:
        form = ClienteForm()
    
    return render(request, 'cadastrar_cliente.html', {'form': form})

def lista_clientes(request):
    # Dados fictícios dos clientes para testes
    clientes = [
        {'nome': 'Cliente A', 'cnpj': '123456789', 'tipo_empresa': 'Tipo 1', 'ativa': True},
        {'nome': 'Cliente B', 'cnpj': '987654321', 'tipo_empresa': 'Tipo 2', 'ativa': False},
        # Adicione mais clientes fictícios conforme necessário
    ]
    # Renderize o template com os dados dos clientes
    return render(request, 'clientes.html', {'clientes': clientes})

# --Motoristas--
def motoristas(request):
    return render(request, 'motoristas.html')

def cadastrar_motorista(request):
    if request.method == 'POST':
        form = MotoristaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('motoristas')  # Redireciona para a lista de motoristas após o cadastro
    else:
        form = MotoristaForm()
    return render(request, 'cadastrar_motorista.html', {'form': form})


# --Multas--
def multas(request):
    return render(request, 'multas.html')

def cadastrar_multa(request):
    if request.method == 'POST':
        form = MultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_multas')  # Redireciona para a página de lista de multas após o cadastro
    else:
        form = MultaForm()
    
    return render(request, 'cadastrar_multa.html', {'form': form})
# --Jornadas--
def jornadas(request):
    return render(request, 'jornadas.html')





