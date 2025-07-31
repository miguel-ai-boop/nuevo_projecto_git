# ventas/urls.py
from rest_framework import routers
from .api import VentaViewSet

router = routers.DefaultRouter()
router.register('api/ventas', VentaViewSet, 'ventas')

urlpatterns = router.urls
