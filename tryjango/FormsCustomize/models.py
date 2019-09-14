from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')
class Product2(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=150)
    price=models.IntegerField()