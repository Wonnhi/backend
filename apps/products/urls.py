from django.urls import path
from .views import get_product

urlpatterns = [
    path('', get_product),
]