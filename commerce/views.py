from django.shortcuts import render
from .models import Products
from .forms import ProductsForm

# Create your views here.

def index(request):
    products = Products.objects.count()
    context = {
        'products' : products
    }
    return render(request, 'commerce/index.html',context)


def product_editar(request,id):
    product = get_object_or_404(Product,id=id)
   
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_listar')
    else:
        form = ProductForm(instance=product)

    return render(request,'commerce/form_product.html',{'form':form})


def product_remover(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_listar') 


def product_criar(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductFormrm()
    else:
        form = ProductForm()

    return render(request, "commerce/form_product.html", {'form': form})


def product_listar(request):
    products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request, "commerce/admin.html",context)

def product(request):
    products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request, "commerce/product.html",context)