from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import ImagenesInicio,ImagenesCertificados,ImagenesRed
from django.template import RequestContext

class Inicio(TemplateView):
	#template_name = "blog/index.html"

	def get(self, request, *args, **kwargs):
		#de esta manera solo seleccionamos el primer valor
		datos = ImagenesInicio.objects.all()[0]
		ctx = {'datos': datos}

		return render(request,'blog/index.html', ctx, context_instance=RequestContext(request))

class Portafolio(TemplateView):
	#template_name = "blog/portafolio.html"

	def get(self, request, *args, **kwargs):
		imgRed = ImagenesRed.objects.all()
		ctx = {'imgRed': imgRed}

		return render(request, 'blog/portafolio.html',ctx, context_instance=RequestContext(request))

class Certificados(TemplateView):
	#template_name = "blog/certificados.html"

	def get(self, request, *args, **kwargs):
		certi = ImagenesCertificados.objects.all()
		ctx = {'certificados':certi}

		return render(request, 'blog/certificados.html', ctx, context_instance=RequestContext(request))


class Cv(TemplateView):
	template_name = "blog/cv.html"