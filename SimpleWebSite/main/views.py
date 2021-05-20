from django.shortcuts import render
from .models import ProductModel, BasketModel


def index(request):
    products = ProductModel.objects.all()
    return render(request, 'main/index.html', {'products': products})


def about(request):
    return render(request, 'main/about.html')


def product(request, productid):
    curproduct = ProductModel.objects.get(id=productid)
    return render(request, 'main/ProductBase.html', {'curproduct': curproduct})


def basket(request):
    b = BasketModel.objects.all()
    amount = len(b)
    return render(request, 'main/basket.html', {'b': b, 'amount': amount})


def addtocart(request):
    curproduct = ProductModel.objects.get(id=request.POST['product_id'])
    b = BasketModel()
    b.products = curproduct
    b.save()
    return render(request, 'main/ProductBase.html', {'curproduct': curproduct})


def clearcart(request):
    BasketModel.objects.all().delete()
    b = []
    return render(request, 'main/basket.html', {'b': b})
