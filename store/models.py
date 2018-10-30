from django.db import models

# Create your models here.
class Vegetable (models.Model):
    name = models.CharField(max_length = 50 )
    thumbnail = models.ImageField(upload_to='product/vegetables' , default='')
    price = models.PositiveIntegerField()


class Cereal (models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='product/cereals', default='')
    price = models.PositiveIntegerField()


class Fruit (models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='product/fruits', default='')
    price = models.PositiveIntegerField()
