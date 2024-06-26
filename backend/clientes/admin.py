from django.contrib import admin
from .models.cliente import Cliente
from .models.endereco import Endereco
from .models.contato import Contato

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Contato)
