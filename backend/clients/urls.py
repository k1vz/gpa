from django.urls import path
from .views import ClientCreateView, ClientDetailView, ClientListView

urlpatterns = [
	path('', ClientListView.as_view(), name='client-list'),
	path('create/', ClientCreateView.as_view(), name='client-create'),
	path('detail/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
]
