from django.contrib import admin
from .models.client import Client
from .models.address import Address
from .models.contact import Contact

admin.site.register(Client)
admin.site.register(Address)
admin.site.register(Contact)
