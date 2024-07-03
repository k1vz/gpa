from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('clients/', include('clients.urls')),
    path('tickets/', include('tickets.urls')),
    path('drivers/', include('drivers.urls')),
	path('', HomeView.as_view(), name='home')
]
