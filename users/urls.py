from django.urls import path
from .views import UserDeleteView, UserDetailView, UserListView, UserLoginView, UserLogoutView, UserRegisterView, UserUpdateView

handler404 = 'app.views.handler404'
handler500 = 'app.views.handler500'

urlpatterns = [
	path('', UserListView.as_view(), name='user-list'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
	path('update/', UserUpdateView.as_view(), name='user-update'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
	path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]