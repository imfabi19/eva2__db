from django.db import models

# ------------------------- Creación de Clases Correspondientes --------------------------------------------
#Creación de Categoria

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique = True)
    tipo = models.CharField(max_length=100)

    class Meta:
        db_table = 'categoria'
        ordering = ['nombre', 'tipo']

    def __str__(self):
        return f"{self.nombre}{self.tipo}"

# Clase Item

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null = True)
    nivel = models.IntegerField(default = 0)
    cantidad = models.IntegerField(default=1)

    pedido = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='pedido')

    categoria = models.ManyToManyField(
        Categoria, related_name='categorias')

    def __str__(self):
        return {self.nombre}

#Clase Personaje

class Personaje(models.Model):
    raza=models.CharField(max_length=100)
    descripcion = models.TextField(null = True)
    nivel = models.IntegerField(defult = 0)
    ban = models.BooleanField(default = False, null = True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Personajes'
        ordering = ['-creado']

    def __str__(self):
        return f"{self.raza}{self.descripcion}"

#Clase Cuenta
class Cuenta(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def str(self):
        return f"{self.nombre}{self.correo}"
