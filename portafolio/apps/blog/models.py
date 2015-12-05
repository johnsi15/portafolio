from django.db import models

class ImagenesInicio(models.Model):
	nombre = models.CharField(max_length=30, blank=True)
	imagen = models.ImageField(upload_to='imgInicio')

	def __unicode__(self):
		return self.nombre

	def traer_url_imagenes(self):
		return 'http://localhost:8000/media/%s' % self.imagen

class ImagenesCertificados(models.Model):
	nombre = models.CharField(max_length=30)
	imagen = models.ImageField(upload_to='imgCertificados')

	def __unicode__(self):
		return self.nombre

class ImagenesRed(models.Model):
	nombre = models.CharField(max_length=30)
	imagen = models.ImageField(upload_to='imgRed')

	def __unicode__(self):
		return self.nombre
