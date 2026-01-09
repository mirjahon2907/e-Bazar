from django.shortcuts import render
from django.views import View
from products.models import Product


class IndexView(View):
    def get(self,requests):
        products = Product.objects.all()
        return render(requests, "index.html", {'products': products})
