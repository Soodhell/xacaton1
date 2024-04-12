from django.urls import path
from .views import *


urlpatterns = [
    path('', RoutelineList.as_view(), name='route'),
    path('create/', RouteCreate.as_view(), name='create_route'),
    path('update/<int:pk>/', RouteUpdate.as_view(), name='update_route'),
]
