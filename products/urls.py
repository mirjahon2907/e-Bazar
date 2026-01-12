from django.urls import path
from .views import new_product, product_detail, product_update, product_delele, new_comment, comment_delete

app_name = 'products'
urlpatterns = [
    path('new', new_product, name='new'),
    path('<int:id>/detail', product_detail, name='product_detail'),
    path('<int:id>/update', product_update, name='product_update'),
    path('<int:id>/delete', product_delele, name='product_delete'),
    path('<int:id>/comment/new', new_comment, name='new_comment'),
    path('<int:id>/comment/<int:comment_id>/delete', comment_delete, name='comment_delete'),
]