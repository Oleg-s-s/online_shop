from django.shortcuts import render, redirect
from .models import Goods
from .forms import GoodsForm

def index(request):
    goods = Goods.objects.order_by('-date_added')
    good = goods[:4]
    data =  {
        'title': 'Eshop',
        'goods': good
    }
    return render(request, 'shop_app/index.html', data)

def catalog(request):
    goods = Goods.objects.order_by('date_added')
    data =  {
        'title': 'Catalog',
        'goods': goods
    }
    return render(request, 'shop_app/catalog.html', data)

def about(request):
    data = {
        'title': 'About'
    }
    return render(request, 'shop_app/about.html', data)

def new_goods(request):
    if request.method != 'POST':
        form = GoodsForm()
    else:
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop_app:catalog')
    data = {
        'form': form,
        'title': 'Add product'
    }
    return render(request, 'shop_app/new_goods.html', data)

def goods(request, goods_id):
    goods =Goods.objects.get(id=goods_id)
    data = {
        'goods': goods,
        'title': goods,
    }
    return render(request, 'shop_app/goods.html', data)