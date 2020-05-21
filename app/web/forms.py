from django import forms
from tinymce.widgets import TinyMCE
from app.web.models import *
class ProductoForm(forms.ModelForm):
    p_descripcion = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Producto
        fields = ('__all__')

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
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = (
            'ct_activo',
            )