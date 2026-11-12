# 🛒 Calculadora de Supermercado em Python

Aplicação de terminal desenvolvida em Python para acompanhar compras de supermercado e controlar o orçamento em tempo real.

## Funcionalidades

- Adicionar produtos com preço unitário e quantidade
- Aceitar quantidades fracionadas (por exemplo, 0,5 kg de carne)
- Aceitar vírgula como separador decimal
- Exibir carrinho tabulado, total e saldo disponível
- **Desfazer**: remover o último produto
- **Remover**: selecionar um produto pelo número
- **Acabei**: mostrar o resumo final e encerrar
- Validar entradas numéricas e avisar quando o orçamento for ultrapassado

## Como executar

Requer Python 3.8 ou superior. Não utiliza bibliotecas externas.

```bash
git clone https://github.com/luskywarrior/calculadora-supermercado.git
cd calculadora-supermercado
python3 calcsup.py
```

Informe o orçamento inicial e depois o nome, preço e quantidade de cada produto. Para terminar, digite `Acabei`.

### Exemplo

```text
Orçamento: R$ 100,00
Produto: Carne
Quanto custa? R$ 45,90
Quantos vai levar?: 0,5

PRODUTO                 QTDE      UNIDADE        TOTAL
Carne                    0,5        45,90        22,95

Gastou:    R$ 22,95
Saldo:     R$ 77,05
```

## Testes

```bash
python3 -m unittest discover -s tests -v
```

## Tecnologias e conceitos

Python, listas, dicionários, funções, laços, tratamento de exceções e formatação de dados.

## Próximas melhorias

- Cálculos monetários com `decimal.Decimal`
- Unidade de medida (kg, un, L)
- Interface gráfica e versão Android

Projeto de estudo e portfólio, em evolução.
