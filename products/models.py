from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=17)
    tg_username = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f"{self.product}"

    

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Comment by {self.author.username} on {self.product.title}'