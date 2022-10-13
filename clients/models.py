from django.db import models

# Create your models here.
class Clients(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

class Address(models.Model):
    street = models.CharField(max_length=200)
    number = models.IntegerField()
    city = models.CharField(max_length=200)
    zip = models.IntegerField()
    country = models.CharField(max_length=200)
    client = models.ForeignKey(Clients, related_name='addresses', null=True, on_delete=models.SET_NULL)