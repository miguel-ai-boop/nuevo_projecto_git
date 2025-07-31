"""
URL configuration for Miniom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from producto.api import CategoriaViewSet, ProductoViewSet
from usuarios.api import UsuarioViewSet  # importa el viewset de usuarios
from ventas.api import VentaViewSet      # importa el viewset de ventas

router = routers.DefaultRouter()
router.register('api/categories', CategoriaViewSet, 'categories')
router.register('api/products', ProductoViewSet, 'products')
router.register('api/users', UsuarioViewSet, 'users')
router.register('api/sales', VentaViewSet, 'sales')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
