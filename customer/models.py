from django.db import models
from users.models import User

# Create your models here.
class Category(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    

    class Meta:
        verbose_name = " category"
        verbose_name_plural = " categories"
        ordering = ["-id"]
        db_table = "category"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=255)
    image=models.ImageField(upload_to="product")
    price=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    class Meta:
        verbose_name = " product"
        verbose_name_plural = " products"
        ordering = ["-id"]
        db_table = "product"    

    def __str__(self):
        return self.name