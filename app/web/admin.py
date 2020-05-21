from django.contrib import admin
from app.web.models import *
from app.web.forms import *
from django.contrib import messages
# Register your models here.



class ProductoConfig(admin.ModelAdmin):
    form = ProductoForm

class BlogConfig(admin.ModelAdmin):
    form = BlogForm
    filter_horizontal = ('blog_tags',) 
    actions = ['activar_portada']
    def save_model(self, request, obj, form, change):
        obj.blog_pertenece = request.user
        super().save_model(request, obj, form, change)
    def activar_portada(self, request, queryset):
        if len(queryset) == 1:
            Blog.objects.all().update(blog_portada=False)
            port=queryset.update(blog_portada=True)
            messages.success(request, 'Portada actualizada {}.'.format(port))
        else:
            messages.warning(request, 'Solo debe seleccionar un elemento.')
    activar_portada.short_description = "Activar como portada"


class ContactoConfig(admin.ModelAdmin):
    form = ContactoForm
    actions = ['activar_contacto']
    def activar_contacto(self, request, queryset):
        if len(queryset) == 1:
            Contacto.objects.all().update(ct_activo=False)
            queryset.update(ct_activo=True)
            messages.success(request, 'Activacion modulo de contacto.')
        else:
            messages.warning(request, 'Solo debe seleccionar un elemento.')
    activar_contacto.short_description = "Activar contacto"
    
admin.site.register(Galeria)
admin.site.register(Marca)
admin.site.register(CatDepo)
admin.site.register(Producto, ProductoConfig)
admin.site.register(Pedido)
admin.site.register(BanerPrincipal)
admin.site.register(Blog, BlogConfig)
admin.site.register(Tag)
admin.site.register(Contacto, ContactoConfig)