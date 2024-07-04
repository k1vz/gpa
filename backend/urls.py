from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('users/', include('users.urls')),
    path('clients/', include('clients.urls')),
    path('tickets/', include('tickets.urls')),
    path('drivers/', include('drivers.urls')),
	path('', HomeView.as_view(), name='home')
]
