from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta: #To save this new form in the admin database
		model = User
		fields = ["username", "email", "password1", "password2"]