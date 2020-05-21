from django.db import models
from django.conf import settings
Usuario = settings.AUTH_USER_MODEL
from django.utils.html import mark_safe

class Galeria(models.Model):
    g_image=models.ImageField(verbose_name="Imagen", upload_to="galeria/")
    g_aternativo=models.CharField(verbose_name="Texto alternativo", max_length=300)
    class Meta:
        verbose_name = "Venta - Galeria"
        verbose_name_plural = "Venta - Galerias"
    def __str__(self):
        return str(self.g_image)
    def img_view(self):
        return mark_safe("""<img src="{}" alt="{}" style="width: 80px; height: 60px;">""".format(self.g_image.url, self.g_aternativo))
class Marca(models.Model):
    m_nombre=models.CharField(verbose_name="Nombre", max_length=100)
    m_visible=models.BooleanField(verbose_name="Activar", default=True)
    def __str__(self):
        return self.m_nombre
    class Meta:
        verbose_name = "Venta - Marca"
        verbose_name_plural = "Venta - Marcas"

class CatDepo(models.Model):
    cd_nombre=models.CharField(verbose_name="Nombre", max_length=100)
    cd_img=models.ImageField(verbose_name="imagen destacada", upload_to="img/categoria_departamento", help_text="Tamaños recomendados alto:270px, ancho:270px")
    cd_visible = models.BooleanField(verbose_name="Activar", default=True)
    def __str__(self):
        return self.cd_nombre
    class Meta:
        verbose_name = "Venta - Categoria/Departamento"
        verbose_name_plural = "Venta - Categorias/Departamentos"

IVA=((0.0, 'SIN IVA'), (0.16, '16%'))

class Producto(models.Model):
    p_nombre=models.CharField(verbose_name="Nombre de producto", max_length=350)
    p_descripcion=models.TextField('Descripcion enriquecido para sitio web', blank=True, null=True)
    p_precio=models.FloatField(verbose_name="Precio")
    p_existencia=models.IntegerField(verbose_name="Existencia")
    p_descuento=models.IntegerField(verbose_name="Porcentaje de descuento", help_text="Numeros enteros del 1 al 100, si no desea añadir deje tal cual esta.", default=0)
    p_activo=models.BooleanField(verbose_name="Producto visible", default=True)    
    p_foto=models.ImageField(verbose_name="Foto principal", upload_to="producto/img/")
    p_galeria=models.ManyToManyField(Galeria, verbose_name="Galeria adicional", help_text="Si desea agregar imagenes adicionales")
    p_fecha=models.DateTimeField(auto_now_add=True)
    p_vender_s_stock=models.BooleanField(verbose_name="Vender sin descontar stock", help_text="Vender producto sin importar existencia.", default=False)
    p_iva=models.FloatField(verbose_name="Iva", choices=IVA)
    def __str__(self):
        return self.p_nombre
    class Meta:
        verbose_name = "Venta - Producto"
        verbose_name_plural = "Venta - Productos"

STATUS=[
    (1, "CREADO"),
    ]
class Pedido(models.Model):
    p_id=models.BigAutoField(primary_key=True)
    p_fecha=models.DateTimeField(verbose_name="Fecha de pedido", auto_now_add=True)
    p_status=models.IntegerField(choices=STATUS, default=1, verbose_name="Estado de pedido")
    def __str__(self):
        return str(self.p_id)
    class Meta:
        verbose_name = "Venta - Pedido"
        verbose_name_plural = "Venta - Pedido"


class DetallePedido(models.Model):
    dtl_id=models.BigAutoField(primary_key=True)
    dtl_pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=True, null=True, verbose_name="N° pedido")
    dtl_producto=models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    dtl_precio=models.FloatField(verbose_name="Precio")
    dtl_cantidad=models.IntegerField(verbose_name="Cantidad")
    dtl_user_add=models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name="Usuario creó")
    dtl_finalizado=models.BooleanField(default=False)
    def __str__(self):
        return str(self.dtl_id)

SOCIAL=[
    ('<i class="fa fa-facebook"></i>', 'Facebook'),
    ('<i class="fa fa-twitter"></i>', 'Twitter'),
    ('<i class="fa fa-linkedin"></i>', 'Linkedin'),
    ('<i class="fa fa-pinterest-p"></i>', 'Pinterest'),
    ('<i class="fa fa-instagram"></i>', 'Instagram"'),
    ('1', 'Email'),
    ('2', 'Info de envio'),
    ('3', 'Telefono'),
]
class BanerPrincipal(models.Model):
    bp_tipo=models.CharField(verbose_name="Tipo de red social", max_length=500, choices=SOCIAL, unique=True)
    bp_url=models.CharField(verbose_name="Contenido", max_length=800, help_text="Puede ser la info de envio, url, email o numero de telefono")
    def __str__(self):
        return self.get_bp_tipo_display()
    class Meta:
        verbose_name = "Config - Baner Principal"
        verbose_name_plural = "Config - Baner Principales"
 

class Tag(models.Model):
    tag_nombre=models.CharField(verbose_name="Tag", max_length=70, unique=True)
    def __str__(self):
        return self.tag_nombre
    class Meta:
        verbose_name = "Blog - Tag"
        verbose_name_plural = "Blog - Tags"

class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    blog_titulo =models.CharField('Titulo', max_length=600, help_text="Si desea añadir salto de linea escriba &lt;br&gt;")
    blog_descripcion =models.CharField('Descripcion', max_length=2000)
    blog_contenido=models.TextField('Contenido', blank=False, null=True,)
    blog_imagen = models.ImageField('Imagen Blog', upload_to='img_blogs/', help_text="Imagen destacada del blog. Medidas sugeridas para portada; altura:431px - Anchura:870px")
    blog_creado=models.DateTimeField('Creado en', auto_now_add=True)
    blog_ultima_actualizacion=models.DateTimeField('Ultima Actualizacion', auto_now=True)
    blog_pertenece=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    blog_tags=models.ManyToManyField(Tag, verbose_name="Tags relacionados")
    blog_categoria=models.ForeignKey(CatDepo, on_delete=models.CASCADE, verbose_name="Categoria a la que pertenece")
    blog_portada=models.BooleanField(verbose_name="Activar como portada", default=False)
    
    def __str__(self):
        return self.blog_titulo
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs" 


class Contacto(models.Model):
    ct_telefono=models.CharField(verbose_name="Telefono de contacto", max_length=13)
    ct_direccion=models.CharField(verbose_name="Direccion del local", max_length=400)
    ct_apertura=models.CharField(verbose_name="Hora de apertura y cierre", max_length=400, help_text="Ejemplo 10:00 am - 23:00 pm")
    ct_email=models.EmailField(verbose_name="Email", max_length=300, help_text="Correo electronico")
    ct_iframe_maps=models.CharField(verbose_name="Iframe de mapa", max_length=3000, help_text="Iframe que puede obtener del google maps")
    ct_activo=models.BooleanField(default=False, verbose_name="Activar contacto")
    ct_form=models.BooleanField(verbose_name='Formulario', help_text="Desea activar formulario de contacto.")
    def __str__(self):
        return self.ct_direccion
    class Meta:
        verbose_name = "Config - Contacto"
        verbose_name_plural = "Config - Contacto"

