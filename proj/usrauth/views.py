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


def signUpView(request):
	
	msg = ""
	success = False

	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			first_name = form.cleaned_data.get('first_name')
			password = form.cleaned_data.get('password1')
			email = form.cleaned_data.get('email')
			user = authenticate(email=email, password=password)

			msg = "User created"
			success = True

			return redirect("../../usrauth/profile")
		else:
			msg = "form is not valid"
	else:
		form = forms.SignUpForm()

	return render(request, 'usrauth/register.html', {'form':form, 'msg':msg, "success":success})
