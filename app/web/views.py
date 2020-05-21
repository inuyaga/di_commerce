from django.shortcuts import render
from django.views.generic import TemplateView, ListView, TemplateView, ListView
from app.web.models import *
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class IndexView(TemplateView):
    template_name = "web/inicio.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portada']=Blog.objects.filter(blog_portada=True).first()
        context['cat_depo']=CatDepo.objects.filter(cd_visible=True)
        context['blogs']=Blog.objects.exclude(blog_portada=True).order_by('-blog_creado')[:6]
        return context

class ComprarListView(ListView):
    model = Producto
    template_name = "web/comprar.html" 


class LoginViewWeb(LoginView):
    template_name = "web/login.html"

class SalirViewWeb(LogoutView):
    template_name = "web/salir.html"


class ContactoView(TemplateView):
    template_name = "web/contacto.html"    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacto']=Contacto.objects.filter(ct_activo=True)[:1]
        return context

class BlogListView(ListView):
    model = Blog
    paginate_by = 6
    template_name="web/blog_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria']=CatDepo.objects.all()
        context['blog_recientes']=Blog.objects.all().order_by('-blog_creado')[:3]
        context['tags']=Tag.objects.all().order_by('tag_nombre')
        return context
    
    