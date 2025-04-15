"""
Testes da classe Produto.
"""
import unittest
from datetime import datetime, timedelta

from produto import Produto


class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        self.produto = Produto(
            codigo="123",
            nome="Feijão",
            preco=10.0,
            quantidade=20,
            data_validade=datetime.now() + timedelta(days=30),
            estoque_minimo=10
        )

    def test_inicializacao(self):
        self.assertEqual(self.produto.codigo, "123")
        self.assertEqual(self.produto.nome, "Feijão")
        self.assertEqual(self.produto.preco, 10.0)
        self.assertEqual(self.produto.quantidade, 20)


    def test_adicionar_estoque(self):
        self.produto.adicionar_estoque(10)
        self.assertEqual(self.produto.quantidade, 30)        

    def test_remover_estoque(self):
        resultado = self.produto.remover_estoque(5)
        self.assertTrue(resultado)
        self.assertEqual(self.produto.quantidade, 15)

        resultado_falha = self.produto.remover_estoque(100)
        self.assertFalse(resultado_falha)        

    def test_verificar_estoque_baixo(self):
        self.produto.quantidade = 5
        self.assertTrue(self.produto.verificar_estoque_baixo())

        self.produto.quantidade = 15
        self.assertFalse(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        self.assertEqual(self.produto.calcular_valor_total(), 200.0)

    def test_verificar_validade(self):
        self.assertTrue(self.produto.verificar_validade())

        self.produto.data_validade = datetime.now() - timedelta(days=1)
        self.assertFalse(self.produto.verificar_validade())


if __name__ == "__main__":
    unittest.main() 