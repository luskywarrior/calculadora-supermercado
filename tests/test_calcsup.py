import unittest
from decimal import Decimal

from calcsup import calcular_total, formatar_moeda


class TestCalculadora(unittest.TestCase):
    def test_total_com_quantidade_fracionada(self):
        carrinho = [
            {"Produto": "Carne", "Valor Unitário": Decimal("45.90"), "Quantidade": Decimal("0.5")},
            {"Produto": "Arroz", "Valor Unitário": Decimal("25.90"), "Quantidade": Decimal("2")},
        ]
        self.assertEqual(calcular_total(carrinho), Decimal("74.75"))

    def test_carrinho_vazio(self):
        self.assertEqual(calcular_total([]), Decimal("0.00"))

    def test_formatacao_brasileira(self):
        self.assertEqual(formatar_moeda(Decimal("1234.5")), "1.234,50")


if __name__ == "__main__":
    unittest.main()
