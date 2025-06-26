from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ClienteViewSet, AnimalViewSet, PedidoAdocaoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'animais', AnimalViewSet)
router.register(r'pedidos', PedidoAdocaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
