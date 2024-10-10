from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    country = models.CharField(default="IN" , max_length=100)

    def __str__(self):
        return self.brand_name
    
class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
    product_name = models.CharField(max_length=100)

