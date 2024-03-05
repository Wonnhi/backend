from django.shortcuts import render
from .models import Reviews

def get_reviews(request):
    reviews = Reviews.objects.all()
    return render(request, {'reviews': reviews})
