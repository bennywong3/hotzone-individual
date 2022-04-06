from django.db import models

class Geodata(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    Xcoor = models.DecimalField(max_digits=20, decimal_places=10)
    Ycoor = models.DecimalField(max_digits=20, decimal_places=10)
    def __str__(self):
        return self.name
