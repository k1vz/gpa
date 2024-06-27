from django.urls import path
from .views import UserDetailView, UserListView, UserLoginView, UserLogoutView, UserRegisterView

urlpatterns = [
	path('', UserListView.as_view(), name='user-list'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]