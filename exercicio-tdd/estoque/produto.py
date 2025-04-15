"""
Sistema de controle de estoque.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Produto:
    """Representação básica de um produto no estoque."""

    codigo: str
    nome: str
    preco: float
    quantidade: int = 0
    data_validade: Optional[datetime] = None
    estoque_minimo: int = 10

    def adicionar_estoque(self, quantidade: int) -> None:
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self.quantidade += quantidade

    def remover_estoque(self, quantidade: int) -> bool:
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        if quantidade > self.quantidade:
            return False
        self.quantidade -= quantidade
        return True


    def verificar_estoque_baixo(self) -> bool:
        return self.quantidade < self.estoque_minimo

    def calcular_valor_total(self) -> float:
        return self.preco * self.quantidade

    def verificar_validade(self) -> bool:
        if not self.data_validade:
                return True
        return self.data_validade >= datetime.now()