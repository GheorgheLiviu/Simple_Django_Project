from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):

        return f'{self.name}'