from django.shortcuts import render

def main(request):
    context = {'username': 'vitaly'}
    return render(request, 'mainapp/main.html', context)

def products(request):
    context = {'products': ['SXT', 'LHG', 'RB']}
    return render(request, 'mainapp/products.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')

# Create your views here.
