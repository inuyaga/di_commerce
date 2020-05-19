from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    foto_perfil=models.ImageField('Foto Perfil', upload_to='foto_perfil/')
    fecha_nacimiento=models.DateField('Fecha de nacimiento',null=True, blank=True)
    telefono=models.CharField('Telefono', null=True, blank=True, max_length=10)
    class Meta:
        db_table = 'auth_user' 