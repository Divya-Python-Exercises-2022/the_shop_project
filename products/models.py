from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    picture = models.URLField(default='https://www.freepnglogos.com/uploads/mobile-png/samsung-mobile-png-14.png')
    manufacturer = models.ForeignKey('Manufacturer', null=True, on_delete=models.SET_NULL)  # 'Manufacturer' model name that it is referring to

class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

