from django.urls import path
from . import views
from django.urls import path 

handler404 = 'app.views.handler404'
handler500 = 'app.views.handler500'

urlpatterns = [
    path('motoristas/', views.motoristas, name='motoristas'),
    path('cadastrar-motorista/', views.cadastrar_motorista, name='cadastrar_motorista'),
    path('multas/', views.multas, name='multas'),
    path('cadastrar-multa/', views.cadastrar_multa, name='cadastrar_multa'),
    path('jornadas/', views.jornadas, name='jornadas'),
    path('cadastrar-jornada/', views.cadastrar_jornada, name='cadastrar_jornada'),
]