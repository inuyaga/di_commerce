from django.contrib import admin
from django.urls import path
from app.web import views as WebViews
app_name="web"
urlpatterns = [
    path('', WebViews.IndexView.as_view(), name="inicio"),
    path('comprar/productos', WebViews.ComprarListView.as_view(), name="comprar"),
    path('entrar/', WebViews.LoginViewWeb.as_view(), name="login"),
    path('salir/', WebViews.SalirViewWeb.as_view(), name="salir"),
    path('contacto/', WebViews.ContactoView.as_view(), name="contacto"),
    path('blogs/listar/', WebViews.BlogListView.as_view(), name="blog_list"),
]
