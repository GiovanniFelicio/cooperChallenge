from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from marca.urls import router as marca_router
from carro.urls import router as carro_router

router = routers.DefaultRouter()
router.registry.extend(marca_router.registry)
router.registry.extend(carro_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
