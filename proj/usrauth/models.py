from __future__ import unicode_literals
from django.db import models, transaction
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import (
	AbstractBaseUser, PermissionsMixin, BaseUserManager
)
# Create your models here.
class UserManager(BaseUserManager):

	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("The given email must be set")
		try:
			with transaction.atomic():
				user = self.model(email=email, **extra_fields)
				user.set_password(password)
				user.save(using=self._db)
				return user
		except:
			raise

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_courer', True)
		return self._create_user(email, password=password, **extra_fields)

	def create_courer(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		extra_fields.setdefault('is_courer', True)
		return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
	email 			= 		models.EmailField(max_length=40, unique=True)
	first_name 		= 		models.CharField(max_length=30)
	second_name 	= 		models.CharField(max_length=30, blank=True)
	date_joined 	= 		models.DateTimeField(default=timezone.now)
	profile			=		models.ImageField(upload_to='user/profile', blank=True)
	
	is_courer		=		models.BooleanField(default=False)
	is_active 		= 		models.BooleanField(default=True)
	is_staff 		= 		models.BooleanField(default=False)
	

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name']

	def save(self, *args, **kwargs):
		super(User, self).save(*args, **kwargs)
		return self


	def send_message_to_user(self, theme, message):
		return send_mail(theme, message, 'reddrakosha1@ya.ru', [self.email], fail_silently=False)
