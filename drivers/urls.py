from django.urls import path
from .views.driver import (
	DriverCreateView,
	DriverDetailView,
	DriverListView,
	DriverUpdateView,
	DriverDeleteView
)
from .views.work_period import (
	WorkPeriodListAPIView,
	WorkPeriodCreateAPIView,
	WorkPeriodCreateView,
	WorkPeriodDetailView,
	WorkPeriodListView,
	WorkPeriodUpdateView,
	WorkPeriodDeleteView
)
from .views.daily import (
	DailyCreateView,
	DailyDetailView,
	DailyListView,
	DailyUpdateView,
	DailyDeleteView
)


urlpatterns = [
	path('', DriverListView.as_view(), name='driver-list'),
	path('create/', DriverCreateView.as_view(), name='driver-create'),
	path('detail/<int:pk>/', DriverDetailView.as_view(), name='driver-detail'),
	path('update/<int:pk>/', DriverUpdateView.as_view(), name='driver-update'),
	path('delete/<int:pk>/', DriverDeleteView.as_view(), name='driver-delete'),

	path('work_periods/', WorkPeriodListView.as_view(), name='work-period-list'),
	path('work_periods/api/', WorkPeriodListAPIView.as_view()),
	path('work_periods/create/', WorkPeriodCreateView.as_view(), name='work-period-create'),
	path('work_periods/create/api/', WorkPeriodCreateAPIView.as_view()),
	path('work_periods/detail/<int:pk>/', WorkPeriodDetailView.as_view(), name='work-period-detail'),
	path('work_periods/update/<int:pk>/', WorkPeriodUpdateView.as_view(), name='work-period-update'),
	path('work_periods/delete/<int:pk>/', WorkPeriodDeleteView.as_view(), name='work-period-delete'),

	path('dailies/', DailyListView.as_view(), name='daily-list'),
	path('dailies/create/', DailyCreateView.as_view(), name='daily-create'),
	path('dailies/detail/<int:pk>/', DailyDetailView.as_view(), name='daily-detail'),
	path('dailies/update/<int:pk>/', DailyUpdateView.as_view(), name='daily-update'),
	path('dailies/delete/<int:pk>/', DailyDeleteView.as_view(), name='daily-delete'),
]
