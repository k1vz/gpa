from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('email',)
		labels = {
			'email': 'Email'
		}
