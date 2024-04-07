from django.urls import path
from .views import *


urlpatterns = [
    path('', NewslineList.as_view(), name='main'),
    path('create/', NewslineCreate.as_view(), name='create_news'),
    path('update/<int:pk>/', NewsUpdate.as_view(), name='update_news'),
    path('<int:pk>/', NewsDetail.as_view(), name='news_datail'),
    path('products/', Productslist.as_view(), name='poducts_list'),
    path('ordered_products/<int:pk>/', OrderedProductslist.as_view(), name='ordered_products_list'),
]
