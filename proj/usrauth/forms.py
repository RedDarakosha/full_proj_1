from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from .models import User

class LoginForm(forms.Form):
	email = forms.EmailField(
		widget = forms.TextInput(
			attrs={
				'placeholder':'email',
				'class':'login_field email',
			})
		)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder':'password',
				'class':'login_field password', 
			})
		)


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'how we can name you?',
				'class':'register_field first_name'
			})
		)

	email = forms.EmailField(
		widget = forms.TextInput(
			attrs={
				'placeholder': 'email',
				'class':'register_field email',
			})
		)

	password1 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder':'password',
				'class':'login_field password1', 
			})
		)

	password2 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder':'repeat password',
				'class':'login_field password2', 
			})
		)
	class Meta:
		model = User
		fields = ('first_name', 'email', 'password1', 'password2',)