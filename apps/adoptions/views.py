from rest_framework import viewsets
from .models import Categoria, Cliente, Animal, PedidoAdocao
from .serializers import CategoriaSerializer, ClienteSerializer, AnimalSerializer, PedidoAdocaoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class PedidoAdocaoViewSet(viewsets.ModelViewSet):
    queryset = PedidoAdocao.objects.all()
    serializer_class = PedidoAdocaoSerializer
