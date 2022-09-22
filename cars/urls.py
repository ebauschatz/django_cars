from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_list),
    path('<int:pk>/', views.car_detail),
    path('make/<make>/', views.car_detail_by_make),
    path('color/<color>/', views.car_detail_by_color),
]