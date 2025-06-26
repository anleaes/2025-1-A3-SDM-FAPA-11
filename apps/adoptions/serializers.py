from rest_framework import serializers
from .models import Categoria, Cliente, Animal, PedidoAdocao

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class PedidoAdocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoAdocao
        fields = '__all__'
