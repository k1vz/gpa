from django.shortcuts import render, redirect
from .forms import MotoristaForm
from .models import Frota

# --Motoristas--
def motoristas(request):
    return render(request, 'motoristas.html')
def cadastrar_motorista(request):
    if request.method == 'POST':
        form = MotoristaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('motoristas')
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
            return redirect('base')  # Redireciona para a página base após o cadastro
    else:
        form = MultaForm()
    
    return render(request, 'cadastrar_multa.html', {'form': form})
# --Jornadas--
def jornadas(request):
    return render(request, 'jornadas.html')
def cadastrar_jornada(request):
    if request.method == 'POST':
        form = JornadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_jornadas') 
    else:
        form = JornadaForm()
    return render(request, 'cadastrar_jornada.html', {'form': form})

# "We have a dashboard at home", dashboard at home
def dashboard(request):
    # Lógica para recuperar as informações do dashboard aqui
    # Exemplo de informações fictícias:
    num_motoristas = 50
    num_motoristas_ativos = 40
    frota_total = 100
    frota_ativa = 80
    frota_manutencao = 20
    num_diarios_cadastrados = 200
    num_diarios_assinados_mes = 150
    num_multas_total = 500
    num_multas_ultimo_mes = 50
    num_multas_ativas = 30
    num_motoristas_desativados = 10
    num_multas_terminadas = 200
    context = {
        'num_motoristas': num_motoristas,
        'num_motoristas_ativos': num_motoristas_ativos,
        'frota_total': frota_total,
        'frota_ativa': frota_ativa,
        'frota_manutencao': frota_manutencao,
        'num_diarios_cadastrados': num_diarios_cadastrados,
        'num_diarios_assinados_mes': num_diarios_assinados_mes,
        'num_multas_total': num_multas_total,
        'num_multas_ultimo_mes': num_multas_ultimo_mes,
        'num_multas_ativas': num_multas_ativas,
        'num_motoristas_desativados': num_motoristas_desativados,
        'num_multas_terminadas': num_multas_terminadas,
    }
    return render(request, 'dashboard.html', context)

# Pedro, o dashboard deve estár funcionando, só tem que testar com db, esse código de baixo é o integrado a base de dados
'''def dashboard(request):
    # Var de tempo
    now = datetime.now()
    last_month = now - timedelta(days=30)
    
    # Consulta para obter as informações necessárias
    num_motoristas = Motorista.objects.count()
    num_motoristas_ativos = Motorista.objects.filter(ativo=True).count()
    num_diarios_cadastrados = Jornada.objects.count()
    num_diarios_assinados_mes = Jornada.objects.filter(data_assinatura__month=now.month).count()
    num_multas_total = Multa.objects.count()
    num_multas_mes = Multa.objects.filter(data_infracao__month=now.month).count()
    num_multas_ultimo_mes = Multa.objects.filter(data_infracao__month=last_month.month).count()
    num_multas_ativas = Multa.objects.filter(ativa=True).count()
    
    # Exemplo de cálculo para os demais números
    num_motoristas_desativados = num_motoristas - num_motoristas_ativos
    num_multas_terminadas = num_multas_total - num_multas_ativas
    
    context = {
        'num_motoristas': num_motoristas,
        'num_motoristas_ativos': num_motoristas_ativos,
        'num_diarios_cadastrados': num_diarios_cadastrados,
        'num_diarios_assinados_mes': num_diarios_assinados_mes,
        'num_multas_total': num_multas_total,
        'num_multas_mes': num_multas_mes,
        'num_multas_ultimo_mes': num_multas_ultimo_mes,
        'num_multas_ativas': num_multas_ativas,
        'num_motoristas_desativados': num_motoristas_desativados,
        'num_multas_terminadas': num_multas_terminadas,
    }
    return render(request, 'dashboard.html', context)'''

#Erros
def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def frota(request):
    frota_list = Frota.objects.all()
    return render(request, 'frota.html', {'frota_list': frota_list})

def cadastrar_frota(request):
    if request.method == 'POST':
        form = FrotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frota')  # Redireciona para a página de listagem da frota após o cadastro
    else:
        form = FrotaForm()
    
    return render(request, 'cadastrar_frota.html', {'form': form})