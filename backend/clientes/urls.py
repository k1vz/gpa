from django.urls import path
from .views import ClienteCreateView, ClienteDetailView, ClienteListView

urlpatterns = [
	path('', ClienteListView.as_view(), name='cliente-list'),
	path('create/', ClienteCreateView.as_view(), name='cliente-create'),
	path('detail/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
]
