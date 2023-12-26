from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    types = Product_Type.objects.all()
    sellers = Seller.objects.all()
    warrenty = Warranty.objects.all()
    
    products = Product.objects.all()
    context = {
        'categories' :categories,
        'brands' :brands,
        'types' :types,
        'sellers' :sellers,
        'warranty' :warrenty,
        'products': products
        
    }
    return render(request, 'search_filter/home.html', context)