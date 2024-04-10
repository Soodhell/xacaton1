from django.urls import path
from .views import *


urlpatterns = [
    path('', PickUpPointList.as_view(), name='list_pick_up_point'),
    path('create/', PickUpPointCreate.as_view(), name='create_pick_up_point'),
]