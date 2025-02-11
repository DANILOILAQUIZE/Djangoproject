from django.db import models

# Create your models here.


class Escuela(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    imagen = models.ImageField(upload_to='escuelas/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class ProyectoConstruccion(models.Model):
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name="proyectos")
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre} - {self.escuela.nombre}"

class Plazo(models.Model):
    proyecto = models.ForeignKey(ProyectoConstruccion, on_delete=models.CASCADE, related_name="plazos")
    descripcion = models.CharField(max_length=255)
    fecha_limite = models.DateField()
    completado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.descripcion} - {self.proyecto.nombre}"
