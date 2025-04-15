"""
Testes da classe Funcionario.
"""
import unittest
from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):

    def test_calcular_salario_bruto(self):
        funcionario = Funcionario(
            nome="João", matricula=1,
            salario_hora=50.0, horas_trabalhadas=160
        )
        esperado = 50.0 * 160
        self.assertEqual(funcionario.calcular_salario_bruto(), esperado)

    def test_calcular_custo_total(self):
        funcionario = Funcionario(
            nome="Ana", matricula=2,
            salario_hora=60.0, horas_trabalhadas=100,
            custo_empregador=1200.0, tem_comissao=True,
            valor_comissao=150.0, contratos_fechados=2
        )
        salario = 60.0 * 100
        comissao = 150.0 * 2
        custo_total = salario + comissao + 1200.0
        self.assertEqual(funcionario.calcular_custo_total(), custo_total)

    def test_calcular_comissao(self):
        funcionario_com = Funcionario(
            nome="Maria", matricula=3,
            tem_comissao=True, valor_comissao=200.0, contratos_fechados=5
        )
        self.assertEqual(funcionario_com.calcular_comissao(), 1000.0)

        funcionario_sem = Funcionario(
            nome="Carlos", matricula=4,
            tem_comissao=False, valor_comissao=300.0, contratos_fechados=10
        )
        self.assertEqual(funcionario_sem.calcular_comissao(), 0.0)


if __name__ == "__main__":
    unittest.main()
