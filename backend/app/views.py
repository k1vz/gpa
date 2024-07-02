from django.shortcuts import render, redirect
from clients.models.client import Client, Address, Contact
from .forms import ClienteForm, MotoristaForm, MultaForm, JornadaForm, FrotaForm

#--Login--
def login_view(request):
    # Lógica de autenticação
    if request.method == 'POST':
        # Aqui você pode verificar os dados de login, por exemplo:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Lógica de autenticação (geralmente você fará isso com o Django Auth)
        # Por exemplo:
        if email == 'usuario' and senha == 'senha':
            # Autenticação bem-sucedida, redirecionar para a página 'base'
            return redirect('base')
        else:
            # Se a autenticação falhar, pode adicionar uma mensagem de erro
            # Ou qualquer outra lógica que desejar
            return render(request, 'login.html', {'erro': True})
    
    # Se não for um POST, renderiza o formulário de login
    return render(request, 'login.html')


# --Base--
def base_view(request):
    return render(request, 'base.html')


# --Clientes--
def clientes(request):
    return render(request, 'clientes.html')

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = Client(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return redirect('clientes')  # Redireciona para a página de listagem de clientes
    else:
        form = ClienteForm()
    
    return render(request, 'cadastrar_cliente.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    contacts = Contact.objects.all()
    addresses = Address.objects.all()

    context = {
        'clients': clients,
        'contacts': contacts,
        'addresses': addresses
    }

    return render(request, 'cadastrar_cliente.html', context)

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


#Frota - Não usado
'''def frota(request):
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
    
    return render(request, 'cadastrar_frota.html', {'form': form})'''