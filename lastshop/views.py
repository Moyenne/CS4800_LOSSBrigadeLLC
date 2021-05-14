from django.shortcuts import render
from .models import cart, driver, favorite, grocerylist, groceryorder, item, paymentinfo, store, suborder, tag, webuser

def about(request):
    context = {
        'items' : item.objects.all(),
    }
    return render(request, 'lastshop/about.html')

def home(request):
    return render(request, 'lastshop/home.html')

def homepage(request):
    return render(request, 'lastshop/HomePage.html')