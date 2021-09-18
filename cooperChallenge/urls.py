from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework import permissions
from marca.urls import router as marca_router
from carro.urls import router as carro_router

router = routers.DefaultRouter()
router.registry.extend(marca_router.registry)
router.registry.extend(carro_router.registry)

schema_view = get_schema_view(
    openapi.Info(
        title="Cooper Challenge API",
        default_version='v1',
        description="API destinada ao desafio proposto pela Coopersystem",
        contact=openapi.Contact(email="gvnnfelicio@gmail.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
