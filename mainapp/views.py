from django.shortcuts import render
import json, os
from .models import Product, ProductCategory

def loadMenuFromJSON():
    with open(os.path.join('mainapp/json/menu.json'), 'r') as infile:
        return json.load(infile)

def main(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu,'username': 'vitaly'}
    return render(request, 'mainapp/main.html', context)

def products(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, 'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()}
    return render(request, 'mainapp/products.html', context)

def contacts(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu}
    return render(request, 'mainapp/contacts.html', context)

