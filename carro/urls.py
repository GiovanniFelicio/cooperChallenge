from rest_framework.routers import DefaultRouter

from carro.api.viewset import CarroViewSet

router = DefaultRouter()
router.register(r'carro', CarroViewSet, basename='carro')
