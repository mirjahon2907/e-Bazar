from django.shortcuts import render
from django.views import View
from products.models import Product, Category
from django.shortcuts import get_object_or_404


def for_all_pages(request):
    categories = Category.objects.all()
    return {'categories':categories}


class IndexView(View):
    def get(self,requests):
        products = Product.objects.all()
        return render(requests, "index.html", {'products': products})


class CategoryView(View):
    def get(self,requests, category_name):
        category = get_object_or_404(Category,name=category_name)
        products = Product.objects.filter(category=category)

        return render(requests, "category.html", {'category': category,'products': products})