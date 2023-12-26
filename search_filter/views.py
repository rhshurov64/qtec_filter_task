from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
import json
from django.template.loader import render_to_string
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


def filter_data(request):
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')
    category = request.GET.getlist('category[]')
    brand = request.GET.getlist('brand[]')
    type = request.GET.getlist('type[]')
    sellers = request.GET.getlist('seller[]')
    warranty = request.GET.getlist('warranty[]')
    # print(sellers)
    # print(type)
    
    products = Product.objects.all()

    if category:
        products = products.filter(category__in=category)

    if brand:
        products = products.filter(brand__in=brand)

    if type:
        products = products.filter(product_type__in=type)

    if sellers:
        products = products.filter(seller__in =sellers)

    if warranty:
        products = products.filter(warranty__in=warranty)
        
    if min_price and max_price:
        products = products.filter(price__range=(min_price, max_price))

    products = products.distinct()
        
        
    data = render_to_string('search_filter/product_list.html', {'products': products})
    return JsonResponse({'data': data})
 