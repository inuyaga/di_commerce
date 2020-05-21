from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.usuario.models import User
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
# from django.contrib import messages
# Register your models here.

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')

class UserConfig(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'foto_perfil', 'fecha_nacimiento', 'telefono')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
admin.site.register(User, UserConfig)
# Register your models here.
