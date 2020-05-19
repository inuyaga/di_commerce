from django.contrib import admin
from django.urls import path
from app.web import views as WebViews
app_name="web"
urlpatterns = [
    path('', WebViews.IndexView.as_view(), name="inicio")
]
