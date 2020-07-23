from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'usrauth'

urlpatterns = [
	path('signup/', signUpView, name='signup'),
	path('login/', login_view, name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('profile/', profile, name='profile'),
]