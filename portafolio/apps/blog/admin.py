from django.contrib import admin

from .models import ImagenesInicio,ImagenesCertificados,ImagenesRed

class ImgInicio(admin.ModelAdmin):
    list_display = ('nombre', 'imagen' ,'imagenes')
    list_filter = ('nombre', )
    search_fields = ('nombre',)

    def imagenes(self, img):
    	url = img.traer_url_imagenes()
    	tag = "<img src=%s >" % url
    	return tag
    #con esta linea de codigo le permitimos mostrar la imagen	
    imagenes.allow_tags = True

class ImgRed(admin.ModelAdmin):
	list_display = ('nombre','imagen')

admin.site.register(ImagenesInicio,ImgInicio)
admin.site.register(ImagenesCertificados)
admin.site.register(ImagenesRed,ImgRed)
