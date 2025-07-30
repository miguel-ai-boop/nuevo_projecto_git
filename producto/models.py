from django.db import models

# Create your models here.

class Categoria(models.Model):

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Producto(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.name