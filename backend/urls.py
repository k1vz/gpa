from .views import HomeView
from django.conf import settings
from django.views.static import serve
from django.urls import path, include, re_path

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('users/', include('users.urls')),
	path('clients/', include('clients.urls')),
	path('tickets/', include('tickets.urls')),
	path('drivers/', include('drivers.urls')),

	re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
	re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
