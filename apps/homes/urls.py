from rest_framework.routers import DefaultRouter
from apps..views import CosmeticsApiViewSet

router = DefaultRouter()

router.register(
    r'cosmetics',
    CosmeticsApiViewSet
)

urlpatterns = router.urls