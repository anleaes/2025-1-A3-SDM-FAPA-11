from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50, blank=True, null=True)
    idade = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)
    disponivel = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='animais')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class PedidoAdocao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    animais = models.ManyToManyField(Animal, related_name='pedidos')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pendente', 'Pendente'), ('Aprovado', 'Aprovado'), ('Recusado', 'Recusado')], default='Pendente')

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente.nome}'
