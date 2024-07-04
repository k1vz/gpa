from .views import HomeView
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import path, include, re_path

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('users/', include('users.urls')),
	path('clients/', include('clients.urls')),
	path('tickets/', include('tickets.urls')),
	path('drivers/', include('drivers.urls')),
]