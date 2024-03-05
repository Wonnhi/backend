from rest_framework.serializer import ModelSerializer
from apps.reviews.models import Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'title',
            'description',
            'photo',
            'created_at',
        ]