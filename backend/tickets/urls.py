from django.urls import path
from .views import (
	TicketCreateView,
	TicketDetailView,
	TicketListView,
	TicketUpdateView,
	TicketDeleteView,
	TicketTypeCreateView,
	TicketTypeDetailView,
	TicketTypeListView,
	TicketTypeUpdateView,
	TicketTypeDeleteView,
)

urlpatterns = [
	path('', TicketListView.as_view(), name='ticket-list'),
	path('create/', TicketCreateView.as_view(), name='ticket-create'),
	path('detail/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
	path('update/<int:pk>/', TicketUpdateView.as_view(), name='ticket-update'),
	path('delete/<int:pk>/', TicketDeleteView.as_view(), name='ticket-delete'),

	path('types/', TicketTypeListView.as_view(), name='ticket-type-list'),
	path('types/create/', TicketTypeCreateView.as_view(), name='ticket-type-create'),
	path('types/detail/<int:pk>/', TicketTypeDetailView.as_view(), name='ticket-type-detail'),
	path('types/update/<int:pk>/', TicketTypeUpdateView.as_view(), name='ticket-type-update'),
	path('types/delete/<int:pk>/', TicketTypeDeleteView.as_view(), name='ticket-type-delete'),
]
