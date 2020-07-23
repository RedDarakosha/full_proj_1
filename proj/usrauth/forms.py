from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from .models import User

class LoginForm(forms.Form):
	email = forms.EmailField(
		widget = forms.TextInput(
			attrs={
				'placeholder':'email',
				'class':'form_field email',
			})
		)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder':'password',
				'class':'form_field password', 
			})
		)