import unittest

from calcsup import calcular_total, formatar_moeda


class TestCalculadora(unittest.TestCase):
    def test_total_com_quantidade_fracionada(self):
        carrinho = [
            {"Produto": "Carne", "Valor Unitário": 45.90, "Quantidade": 0.5},
            {"Produto": "Arroz", "Valor Unitário": 25.90, "Quantidade": 2},
        ]
        self.assertAlmostEqual(calcular_total(carrinho), 74.75)

    def test_carrinho_vazio(self):
        self.assertEqual(calcular_total([]), 0)

    def test_formatacao_brasileira(self):
        self.assertEqual(formatar_moeda(1234.5), "1.234,50")


if __name__ == "__main__":
    unittest.main()
