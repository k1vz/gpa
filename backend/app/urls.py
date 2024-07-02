"""
URL configuration for frontend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.urls import path 
from django.conf.urls import handler404, handler500

#Erros
handler404 = 'app.views.handler404'
handler500 = 'app.views.handler500'

#Outros caminhos
urlpatterns = [
    path('base/', views.base_view, name='base'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('cadastrar-cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('motoristas/', views.motoristas, name='motoristas'),
    path('cadastrar-motorista/', views.cadastrar_motorista, name='cadastrar_motorista'),
    path('frota/', views.frota, name='frota'),
    path('cadastrar-frota/', views.cadastrar_frota, name='cadas_frota'),
    path('multas/', views.multas, name='multas'),
    path('cadastrar-multa/', views.cadastrar_multa, name='cadastrar_multa'),
    path('jornadas/', views.jornadas, name='jornadas'),
    path('cadastrar-jornada/', views.cadastrar_jornada, name='cadastrar_jornada'),
]