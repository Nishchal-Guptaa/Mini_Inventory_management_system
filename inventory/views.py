from django.shortcuts import render, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products':products})

def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name = request.POST['name'],
            sku = request.POST['sku'],
            quantity = request.POST['quantity'],
            price = request.POST['price'],
        )
        return redirect('/')
    return render(request, 'add_product.html')

def delete_product(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/')

def update_stock(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.quantity = request.POST['quantity']
        product.save()
        return redirect('/')
    return render(request, 'update_stock.html', {'product': product})
