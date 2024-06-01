from django.contrib import admin
from django.urls import path, include
# from clientes.views import CreateUserView
# from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView

urlpatterns = [
    path('admin/', admin.site.urls),
	# path('clientes/user/register/', CreateUserView.as_view(), name='register'),
	# path('clientes/token/', TokenObtainSlidingView.as_view(), name='get_token'),
	# path('clientes/token/refresh/', TokenRefreshSlidingView.as_view(), name='refresh'),

	path('clientes-auth/', include('rest_framework.urls')),
    path('clientes/', include('clientes.urls')),
    path('clientes/', include('usuarios.urls')),	
]
