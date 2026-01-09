from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=17)
    tg_username = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')


    def __str__(self):
        return self.username
    


class Saved(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Comment by {self.author.username} on {self.product.title}'