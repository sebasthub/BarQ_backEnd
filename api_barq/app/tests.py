from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Estabelecimento,Mesa, Categoria, Consumidor, Produto
from django.urls import reverse
import pdb

# Create your tests here.
class EstabelecimentoAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('estabelecimento')
        self.estab_data = {
            "nome": "jonaas",
            "endereco": "rua do ze dirceu 14 kk",
            "usuario": "yamete",
            "senha": "o my love",
            "email": "sebas@gmail.com"
        }
    
    def test_create_estabelecimento(self):
        response = self.client.post(self.url, self.estab_data)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Estabelecimento.objects.count(), 1)
        self.assertEqual(Estabelecimento.objects.get().nome, 'jonaas')

    def test_get_estabelecimento(self):
            response = self.client.get(self.url)
            #pdb.set_trace()
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        return super().tearDown()
    

class MesaAPITestCase(TestCase):
    def setUp(self):
        insert_estabelecimento()
        self.client = APIClient()
        self.url = reverse('mesa')
        self.mesa_data = {
            "estabelecimento": 1
            }
        
    def test_create_mesa(self):
        response = self.client.post(self.url, self.mesa_data)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_estabelecimento(self):
        response = self.client.get(self.url)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ProdutoAPITestCase(TestCase):
    def setUp(self):
        insert_estabelecimento()
        insert_categoria()
        self.client = APIClient()
        self.url = reverse('produtos')
        self.produto_data = {
            "nome": "call me jone wallker",
            "descricao": "wiski krai",
            "preco": 12.00,
            "promocao": 0,
            "imagem": "alguma ai",
            "estabelecimento": 1,
            "categoria": 1
        }
    def test_create_produto(self):
        response = self.client.post(self.url, self.produto_data)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_produto(self):
        response = self.client.get(self.url)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ConsumidorAPITestCase(TestCase):
    def setUp(self):
        estabelecimento = insert_estabelecimento()
        insert_mesa(estabelecimento)
        self.client = APIClient()
        self.url = reverse('consumidor')
        self.produto_data = {
            "nome": "call me maybe",
            "mesa": 1
        }

    def test_create_consumidor(self):
        response = self.client.post(self.url, self.produto_data)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_consumidor(self):
        response = self.client.get(self.url)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoriaAPITestCase(TestCase):
    def setUp(self):
        insert_categoria()
        self.client = APIClient()
        self.url = reverse('categoria')

    def test_get_categoria(self):
        response = self.client.get(self.url)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PedidoAPITestCase(TestCase):
    def setUp(self):
        estabelecimento = insert_estabelecimento()
        mesa = insert_mesa(estabelecimento)
        consumidor = insert_consumidor(mesa)
        insert_produto()
        self.client = APIClient()
        self.url = reverse('pedido')
        self.produto_data = {
            "consumidor": consumidor.pk,
            "status": 'false',
            "total": 50.00,
            "produtos": [1,1]
        }

    def test_create_pedido(self):
        response = self.client.post(self.url, self.produto_data)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_pedido(self):
        response = self.client.get(self.url)
        #pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)




#metodos para inserção de dados
def insert_estabelecimento():
    estabelecimento = Estabelecimento()
    estabelecimento.nome = 'bagui'
    estabelecimento.email = 'sebas@gmail.com'
    estabelecimento.usuario = 'jonas'
    estabelecimento.senha = 'yamete'
    estabelecimento.endereco = 'somewere over the rainbow'
    estabelecimento.save()
    return estabelecimento

def insert_mesa(estabelecimento: Estabelecimento):
    mesa = Mesa()
    mesa.estabelecimento = estabelecimento
    mesa.save()
    return mesa

def insert_categoria():
    cat = Categoria()
    cat.nome = 'sebas'
    cat.imagem = 'sbas'
    cat.save()
    return cat

def insert_consumidor(mesa: Mesa):
    consumidor = Consumidor()
    consumidor.nome = 'POOR'
    consumidor.mesa = mesa
    consumidor.save()
    return consumidor

def insert_produto():
    produto = Produto()
    produto.categoria = insert_categoria()
    produto.estabelecimento = insert_estabelecimento()
    produto.nome = 'produto'
    produto.descricao = 'produto'
    produto.preco = 10.40
    produto.promocao = 0
    produto.imagem = ''
    produto.save()
    return produto