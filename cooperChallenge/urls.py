from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from marca.api.viewset import MarcaViewSet
from carro.api.viewset import CarroViewSet

router = routers.DefaultRouter()
router.register(r'marca', MarcaViewSet)
router.register(r'carro', CarroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
