from django.conf.urls import patterns, include, url
from .views import Inicio,Portafolio,Certificados,Cv

urlpatterns = patterns('',
   url(r'^$', Inicio.as_view(), name="inicio"),
   url(r'^portafolio/$', Portafolio.as_view(), name="portafolio"),
   url(r'^certificados/$', Certificados.as_view(), name="certificados"),
   url(r'^cv/$', Cv.as_view(), name="cv"),
)
