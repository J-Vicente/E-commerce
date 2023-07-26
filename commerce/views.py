from django.shortcuts import render,get_object_or_404,redirect
from .models import Products
from .forms import ProductsForm

# Create your views here.

def index(request):
    products = Products.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'commerce/index.html',context)


def product_editar(request,id):
    product = get_object_or_404(Products,id=id)
   
    if request.method == 'POST':
        form = ProductsForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_listar')
    else:
        form = ProductsForm(instance=product)

    return render(request,'commerce/form_product.html',{'form':form})


def product_remover(request, id):
    product = get_object_or_404(Products, id=id)
    product.delete()
    return redirect('product_listar') 


def product_criar(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ProductsForm()
            return redirect('product_listar')
    else:
        form = ProductsForm()

    return render(request, "commerce/form_product.html", {'form': form})


def product_listar(request):
    products = Products.objects.all()
    context ={
        'products':products
    }
    return render(request, "commerce/admin.html",context)

def product(request, id):
    products = get_object_or_404(Products,id=id)
    context ={
        'products':products
    }
    return render(request, "commerce/product.html",context)