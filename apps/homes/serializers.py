from rest_framework.serializers import ModelSerializer
from apps.homes.models import Cosmetics

class CosmeticsSerializer(ModelSerializer):
    class Meta:
        model = Cosmetics
        fields = [
            'id',
            'title',
            'description',
            'photo',
            'price'
        ]