from django.contrib import admin
from .models import *  
import pandas as pd 

# Register your models here.
class signupData(admin.ModelAdmin):
    list_display=["name", "email", "password"]
admin.site.register(signup,signupData)

class productData(admin.ModelAdmin):
    list_display=["productDetails_id","productDetails_name","productDetails_brand","productDetails_description","productDetails_price","productDetails_discount","productDetails_category","productDetails_stock","is_featured","productDetails_image"]
admin.site.register(productDetail,productData)

class cartData(admin.ModelAdmin):
    list_display=["name","email","phn","address"]
admin.site.register(cartDetail,cartData)