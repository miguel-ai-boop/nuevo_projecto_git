from rest_framework import routers
from .api import CategoriaViewSet, ProductoViewSet

router = routers.DefaultRouter()

# Registramos las rutas para cada ViewSet
router.register('api/categories', CategoriaViewSet, 'categories')
router.register('api/products', ProductoViewSet, 'products')

urlpatterns = router.urls
