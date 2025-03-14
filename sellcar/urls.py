from django.urls import path
from .views import sell_car, car_detail

urlpatterns = [
    path('', sell_car, name='sellcar'),
    path('<int:id>/', car_detail, name='car_detail'),
]
