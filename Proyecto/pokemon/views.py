#from django.shortcuts import render
#from django.views.generic import TemplateView
#import sys
#from flask import Flask,render_template
from django.http import Http404
from django.shortcuts import render
from .models import Usuario



def index(request):
	# all_pokemon
	# context = {all_pokemon : all_pokemon}

	return render(request, 'pokemon/index.html')

def detalles(request, usuario_id):
	all_usuarios = Usuario.objects.all()
	try:
		usuario = Usuario.objects.get(pk=usuario_id)
	except Usuario.DoesNotExist: 
		raise http404("Usuario no existe")
	return render(request, 'pokemon/detalles.html', {'usuario' : usuario})







