from django.db import models
import pandas as pd

# Create your models here.

class signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table="signup"


class login(models.Model):
    username_or_email=models.CharField(max_length=20,unique=True)
    Password=models.CharField(max_length=20)

    class Meta:
        db_table="login"


class productDetail(models.Model):
    productDetails_id = models.CharField(max_length=100,unique=True)
    productDetails_name = models.CharField(max_length=100)
    productDetails_brand = models.CharField(max_length=100)
    productDetails_description = models.TextField(max_length=500,default="Lorem, ipsum ")
    productDetails_price = models.DecimalField(max_digits=10, decimal_places=2)
    productDetails_discount = models.DecimalField(max_digits=3, decimal_places=2,default=0.00)
    productDetails_category = models.CharField(max_length=100 ,default=None)
    productDetails_stock = models.IntegerField(default=1)
    is_featured=models.BooleanField(default=False)
    productDetails_image = models.FileField(
        upload_to="products/",
        max_length=300,
        null=True,
        default=None,
    )
    
    class Meta:
        db_table="productDetail"

class cartDetail(models.Model):
   name=models.CharField(max_length=50)
   email=models.EmailField(max_length=50)
   phn =models.IntegerField(default=None)
   address=models.CharField(max_length=100)
   remember=models.BooleanField(default=False)
   
   class Meta:
       db_table="cartDetail"

