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

urlpatterns = [
    path('', views.base, name='base'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('cadastrar-cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('motoristas/', views.motoristas, name='motoristas'),
    path('cadastrar-motorista/', views.cadastrar_motorista, name='cadastrar_motorista'),
    path('multas/', views.multas, name='multas'),
    path('cadastrar-multa/', views.cadastrar_multa, name='cadastrar_multa'),
    path('jornadas/', views.jornadas, name='jornadas'),
    
]