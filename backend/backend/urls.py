from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clientes/', include('clientes.urls')),
    path('api/usuarios/', include('users.urls')),
]
