from django.urls import path
from .views import *


urlpatterns = [
    path('', BasketlineList.as_view(), name="basket"),
    path('create/', BasketCreate.as_view(), name="basket_create"),
    path('update/<int:pk>/', BasketUpdate.as_view(), name="basket_update"),
    path('<int:pk>/', BasketDetail.as_view(), name="basket_detail"),
]
