from .views import HomeView
from django.urls import path, include

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('users/', include('users.urls')),
	path('clients/', include('clients.urls')),
	path('tickets/', include('tickets.urls')),
	path('drivers/', include('drivers.urls')),
]