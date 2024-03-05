from rest_framework.viewsets import ModelViewSet
from apps.homes.models import Cosmetics
from apps.homes.serializers import CosmeticsSerializer

class CosmeticsApiViewSet(ModelViewSet):
    queryset = Cosmetics.objects.all()
    serializer_class = CosmeticsSerializer

