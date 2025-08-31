
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self): return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse('inventory:detail',args=[str(self.id)])
