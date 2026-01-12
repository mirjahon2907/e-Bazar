from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import NewProductForm, ProductForm
from .models import ProductImage, Product, Category, Comment


@login_required(login_url='login')
def new_product(request):
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(request=request)

            for image in request.FILES.getlist('images'):
                ProductImage.objects.create(
                    product=product,
                    image=image
                )

            messages.success(request, "Successfully created!")
            return redirect('main:index')
    else:
        form = NewProductForm()
    
    print(request.FILES)
    return render(request, 'product_new.html', {'form': form})


        
def product_detail(request, id):
    product = get_object_or_404(Product,id=id)
    category_name = product.category

    category = get_object_or_404(Category,name=category_name)
    products = Product.objects.filter(category=category)

    if 'recently_viewed' in request.session:
        r_viewed = request.session['recently_viewed']
        if not product.id in r_viewed:
            r_viewed.append(product.id)
            request.session.modified = True
    
    else:
        request.session['recently_viewed'] = [product.id,]
        
    return render(request, 'product_detail.html', {'product':product, 'products':products})



@login_required(login_url='login')
def product_update(request, id):
        product = get_object_or_404(Product,id=id)
        if request.user == product.author:
            if request.method == "GET":
                form = ProductForm(instance=product)
                return render(request, 'product_update.html', {'form':form, 'product':product})
            elif request.method == "POST":
                form = ProductForm(instance=product, data=request.POST, files=request.FILES)
                if form.is_valid():
                    form.save()
                    if request.FILES.getlist('images'):
                        ProductImage.objects.filter(product=product).delete()
                        for i in request.FILES.getlist('images'):
                            ProductImage.objects.create(product=product,image=i)

                    messages.success(request, 'Successfully updated')
                    return redirect('products:product_detail', product.id)
                
                return render(request, 'product_update.html', {'form':form, 'product':product})
        else:
            messages.error(request, 'Access denied')
            return redirect("main:index")



@login_required(login_url='login')
def product_delele(request,id):
    product = get_object_or_404(Product,id=id)
    if request.user == product.author:
        if request.method=="POST":
            product.delete()
            messages.error(request, 'Successfully deleted!')
            return redirect("main:index")

        return render(request,'product_delete.html',{'product':product})
    else:
        messages.error(request, 'Access denied')
        return redirect("main:index")
    


@login_required(login_url='login')
def new_comment(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method == "POST":
        Comment.objects.create(
            author = request.user,
            product = product,
            body = request.POST['body'],
        )
        messages.info(request, 'Successfully send')
        return redirect('products:product_detail', id)
    return HttpResponse('add comment')


@login_required(login_url='login')
def comment_delete(request,id, comment_id):
    comment = get_object_or_404(Comment,id=comment_id)

    if request.user == comment.author:
        comment.delete()
        messages.info(request, 'Successfully deleted')

        return redirect('products:product_detail', id)      
    

           
    
    