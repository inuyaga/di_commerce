from django.contrib import admin
from app.web.models import *

from tinymce.widgets import TinyMCE
from django import forms
from django.contrib import messages
# Register your models here.

class ProductoForm(forms.ModelForm):
    p_descripcion = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Producto
        fields = ('__all__')

class ProductoConfig(admin.ModelAdmin):
    form = ProductoForm



class BlogForm(forms.ModelForm):
    blog_contenido = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Blog
        fields = (
            'blog_titulo',
            'blog_descripcion',
            'blog_imagen',
            'blog_tags',
            'blog_categoria',
            'blog_contenido',
            )

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
    
admin.site.register(Galeria)
admin.site.register(Marca)
admin.site.register(CatDepo)
admin.site.register(Producto, ProductoConfig)
admin.site.register(Pedido)
admin.site.register(BanerPrincipal)
admin.site.register(Blog, BlogConfig)
admin.site.register(Tag)
admin.site.register(Contacto)