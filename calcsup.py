from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


CENTAVO = Decimal("0.01")
ZERO = Decimal("0.00")


def arredondar_moeda(valor):
    return valor.quantize(CENTAVO, rounding=ROUND_HALF_UP)


def ler_decimal(mensagem, monetario=False):
    while True:
        try:
            valor = Decimal(input(mensagem).strip().replace(",", "."))
            if not valor.is_finite() or valor <= 0:
                print("⚠️ Digite um número válido maior que zero.")
                continue
            if monetario:
                valor = arredondar_moeda(valor)
                if valor <= ZERO:
                    print("⚠️ Digite um número válido maior que zero.")
                    continue
            return valor
        except InvalidOperation:
            print("⚠️ Digite apenas números válidos!")


def formatar_moeda(valor):
    return f"{arredondar_moeda(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calcular_subtotal(item):
    return arredondar_moeda(item["Valor Unitário"] * item["Quantidade"])


def calcular_total(carrinho):
    return sum((calcular_subtotal(item) for item in carrinho), ZERO)


def mostrar_carrinho(carrinho, orcamento):
    print("\n=============== 🛒 MEU CARRINHO 🛒 ===============")
    print(f'{"PRODUTO":20} {"QTDE":>7} {"UNIDADE":>12} {"TOTAL":>12}')
    print("-" * 55)

    for item in carrinho:
        subtotal = calcular_subtotal(item)
        quantidade = f'{item["Quantidade"]:g}'.replace(".", ",")
        print(
            f'{item["Produto"]:20} '
            f'{quantidade:>7} '
            f'{formatar_moeda(item["Valor Unitário"]):>12} '
            f'{formatar_moeda(subtotal):>12}'
        )

    if not carrinho:
        print("🛒 Seu carrinho está vazio.")

    total = calcular_total(carrinho)
    saldo = arredondar_moeda(orcamento - total)
    print("-" * 55)
    print(f"Orçamento: R$ {formatar_moeda(orcamento)}")
    print(f"Gastou:    R$ {formatar_moeda(total)}")
    print(f"Saldo:     R$ {formatar_moeda(saldo)}")
    if saldo < 0:
        print("⚠️ Atenção! Você ultrapassou seu orçamento.")
    return total


def remover_produto(carrinho):
    if not carrinho:
        print("⚠️ O carrinho está vazio.")
        return

    print("\n🗑️ SELECIONE O PRODUTO PARA REMOVER")
    for indice, item in enumerate(carrinho, start=1):
        print(f'{indice} - {item["Produto"]}')

    while True:
        try:
            escolha = int(input("Número do produto (0 para cancelar): "))
            if escolha == 0:
                print("Remoção cancelada.")
                return
            if 1 <= escolha <= len(carrinho):
                removido = carrinho.pop(escolha - 1)
                print(f'🗑️ {removido["Produto"]} removido com sucesso!')
                return
            print("⚠️ Produto inexistente.")
        except ValueError:
            print("⚠️ Digite um número inteiro válido.")


def main():
    print("💵" * 16)
    print("💰 Calculadora de Supermercado 🛒")
    print('Digite "Acabei" para finalizar.')
    print('Digite "Desfazer" para apagar o último produto.')
    print('Digite "Remover" para escolher um produto.')
    print("Bora lá?")

    orcamento = ler_decimal("Quanto de grana você tem? 💵 R$ ", monetario=True)
    carrinho = []

    while True:
        print()
        nome_produto = input("📦 Escreva o nome do produto: ").strip()
        comando = nome_produto.lower()

        if comando == "acabei":
            print("\n🧾 FINALIZANDO SUA COMPRA...")
            total = mostrar_carrinho(carrinho, orcamento)
            print(f"\n💵 Suas compras deram R$ {formatar_moeda(total)}")
            print("✅ Compra finalizada! Até a próxima! 🛒")
            break

        if comando == "desfazer":
            if carrinho:
                removido = carrinho.pop()
                print(f'🗑️ {removido["Produto"]} removido do carrinho.')
            else:
                print("⚠️ O carrinho está vazio.")
            mostrar_carrinho(carrinho, orcamento)
            continue

        if comando == "remover":
            remover_produto(carrinho)
            mostrar_carrinho(carrinho, orcamento)
            continue

        if not nome_produto:
            print("⚠️ Digite o nome de um produto.")
            continue

        valor = ler_decimal("Quanto custa? R$ ", monetario=True)
        quantidade = ler_decimal("Quantos vai levar?: ")
        produto = {
            "Produto": nome_produto.capitalize(),
            "Valor Unitário": valor,
            "Quantidade": quantidade,
        }
        carrinho.append(produto)
        print(f'✅ {produto["Produto"]} adicionado ao carrinho!')
        mostrar_carrinho(carrinho, orcamento)


if __name__ == "__main__":
    main()
