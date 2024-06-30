from django.urls import path
from .views import ClientCreateView, ClientDeleteView, ClientDetailView, ClientListView, ClientUpdateView

urlpatterns = [
	path('', ClientListView.as_view(), name='client-list'),
	path('create/', ClientCreateView.as_view(), name='client-create'),
	path('detail/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
	path('update/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),
	path('delete/<int:pk>/', ClientDeleteView.as_view(), name='client-delete'),
]
