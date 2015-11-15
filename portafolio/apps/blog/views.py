from django.shortcuts import render
from django.views.generic import TemplateView,ListView

class Inicio(TemplateView):
	template_name = "blog/index.html"

class Portafolio(TemplateView):
	template_name = "blog/portafolio.html"

class Certificados(TemplateView):
	template_name = "blog/certificados.html"

class Cv(TemplateView):
	template_name = "blog/cv.html"