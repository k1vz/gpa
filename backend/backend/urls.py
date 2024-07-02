from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('clients/', include('clients.urls')),
    path('tickets/', include('tickets.urls')),
    path('drivers/', include('drivers.urls')),
    path('', include('app.urls')),
]
