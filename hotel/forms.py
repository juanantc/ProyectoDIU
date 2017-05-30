# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from hotel.models import Reservas

class login_form(forms.ModelForm):
	username = forms.SlugField (max_length=9,label='Usuario')
	password = forms.SlugField (max_length=9,widget=forms.PasswordInput(),label='Contraseña')

	class Meta:
		model  = User
		fields = ('username', 'password')

class reserva_form(forms.ModelForm):
	username = forms.SlugField (max_length=8, label='Usuario')
	password = forms.SlugField (max_length=8,widget=forms.PasswordInput(),label='Contraseña')

	class Meta:
		model  = User
		fields = ('username', 'password')
