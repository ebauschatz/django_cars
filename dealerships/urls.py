from django.urls import path
from . import views

urlpatterns = [
    path('', views.dealership_detail),
    path('<int:pk>/', views.dealership_detail_by_id),
    path('<int:pk>/cars/', views.dealership_get_associated_cars)
]