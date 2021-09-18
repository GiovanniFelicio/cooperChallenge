from rest_framework.routers import DefaultRouter

from marca.api.viewset import MarcaViewSet

router = DefaultRouter()
router.register(r'marca', MarcaViewSet, basename='marca')
