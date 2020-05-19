from django.shortcuts import render
from django.views.generic import TemplateView
from app.web.models import *
# Create your views here.

class IndexView(TemplateView):
    template_name = "web/inicio.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portada']=Blog.objects.filter(blog_portada=True).first()
        context['cat_depo']=CatDepo.objects.filter(cd_visible=True)
        print(context['cat_depo'])
        return context
    