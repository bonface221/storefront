from django.shortcuts import render
from store.models import Product,OrderItem
# from django.db.models import F
# Create your views here.

def say_hello(request):
    # queryset= Product.objects.filter(pk=OrderItem.objects.values('product_id')).order_by('title')
    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id')).order_by('title')

    context = dict(name = 'Mnyesh',products = queryset)

    return render(request,'hello.html',context)
