from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login

def login_view(request):
	form = forms.LoginForm(request.POST or None)
	msg = ""
	if request.method =='POST':
		if form.is_valid():

			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				return redirect("../../usrauth/profile")
			else:
				msg = "Invalid creadentials"
		else:
			msg = "Error validating the form"
	return render(request, 'usrauth/login.html', {'form':form, 'msg':msg})

def profile(request):
	user = request.user
	return render(request, 'usrauth/profile.html', {'user':user})