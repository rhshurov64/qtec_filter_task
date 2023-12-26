from django.contrib import admin
from .models import Category, Brand, Warranty, Seller, Product, Product_Type

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('id','duration',)

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    
@admin.register(Product_Type)
class Product_TypeAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'brand','product_type', 'warranty', 'seller', 'price')
    list_filter = ('category', 'brand', 'warranty','product_type', 'seller')
    search_fields = ('name', 'brand__name', 'seller__name')
    list_editable = ('price',)
