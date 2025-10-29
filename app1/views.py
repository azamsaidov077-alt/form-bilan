from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(
                category_name=form.cleaned_data['category_name'],
                description=form.cleaned_data.get('description'),
                image=form.cleaned_data.get('image')
            )
            messages.success(request, 'Kategoriya muvaffaqiyatli qoshildi!')
            return redirect('add_category')
    else:
        form = CategoryForm()

    return render(request, 'add_category.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})



def add_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            Products.objects.create(
                product_name=form.cleaned_data['product_name'],
                category_id=form.cleaned_data['category_id'],
                unit_price=form.cleaned_data['unit_price'],
                discounted=form.cleaned_data.get('discounted', False),
                image=form.cleaned_data.get('image')
            )
            messages.success(request, 'Mahsulot muvaffaqiyatli qoshildi')
            return redirect('add_product')
    else:
        form = ProductsForm()

    return render(request, 'add_product.html', {'form': form})

def product_list(request):
    products = Products.objects.all()
    return render(request, 'product_list.html', {'products': products})



def add_supplier(request):
    if request.method == 'POST':
        form = SuppliersForm(request.POST)
        if form.is_valid():
            Suppliers.objects.create(
                company_name=form.cleaned_data['company_name'],
                contact_name=form.cleaned_data['contact_name'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city']
            )
            messages.success(request, 'Taminotchi muvaffaqiyatli qoshildi!')
            return redirect('add_supplier')
    else:
        form = SuppliersForm()

    return render(request, 'add_supplier.html', {'form': form})

def suppliers_list(request):
        suppliers = Suppliers.objects.all()
        return render(request, 'suppliers_list.html', {'suppliers': suppliers})


def add_order(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            Orders.objects.create(
                customer_name=form.cleaned_data.get('customer_name'),
                order_date=form.cleaned_data['order_date'],
                required_date=form.cleaned_data['required_date'],
                shipped_date=form.cleaned_data.get('shipped_date')
            )
            messages.success(request, 'Buyurtma muvaffaqiyatli qoshildi!')
            return redirect('add_order')
    else:
        form = OrdersForm()

    return render(request, 'add_order.html', {'form': form})

def order_list(request):
    orders = Orders.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


def delete_category(request,pk):
    cat=Category.objects.get(id=pk)
    cat.delete()
    return redirect('category_list')

def delete_product(request,pk):
    product=Products.objects.get(id=pk)
    product.delete()
    return redirect('product_list')

def delete_supplier(request,pk):
    supplier=Suppliers.objects.get(id=pk)
    supplier.delete()
    return redirect('suppliers_list')

def delete_order(request,pk):
    order=Orders.objects.get(id=pk)
    order.delete()
    return redirect('order_list')
