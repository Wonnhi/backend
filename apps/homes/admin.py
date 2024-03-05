from django.contrib import admin
from apps.homes.models import Cosmetics


admin.site.register(Cosmetics)

# Register your models here.

dict = {
    "id": 1,
    "title": "Косметика",
}

dict2 = {
    "id": 2,
    "title": "Тушь",
}

dict3 = {
    "id": 3,
    "title": "уходовая космет",
}


product = {
    "id": 1,
    "category": 3,
    "title": "dsada",
    "description": "dsada",
    "price": 100
}


