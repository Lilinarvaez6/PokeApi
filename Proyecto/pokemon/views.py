#from django.shortcuts import render
#from django.views.generic import TemplateView
#import sys
#from flask import Flask,render_template

from django.template.response import TemplateResponse
from django.shortcuts import render
import datetime


def index(request):
	now = datetime.datetime.now()
	return render(request, 'pokemon/index.html', {'fecha': now})






