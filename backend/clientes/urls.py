from django.urls import path
from .views import ClienteCreateView, ClienteDetailView, ClienteListView

urlpatterns = [
	path('create/', ClienteCreateView.as_view(), name='cliente-create'),
	path('list/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
	path('', ClienteListView.as_view(), name='cliente-list'),
]
