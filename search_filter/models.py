from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Warranty(models.Model):
    duration = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.duration
    

class Seller(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class Product_Type(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True, null = True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank = True, null = True)
    product_type = models.ForeignKey(Product_Type, on_delete=models.CASCADE, blank = True, null = True)
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE, blank = True, null = True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank = True, null = True)
    price = models.DecimalField(max_digits=100, decimal_places=4)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name