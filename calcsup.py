import math


def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
            if not math.isfinite(valor) or valor <= 0:
                print("⚠️ Digite um número válido maior que zero.")
                continue
            return valor
        except ValueError:
            print("⚠️ Digite apenas números válidos!")


def formatar_moeda(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calcular_total(carrinho):
    return sum(item["Valor Unitário"] * item["Quantidade"] for item in carrinho)


def mostrar_carrinho(carrinho, orcamento):
    print("\n=============== 🛒 MEU CARRINHO 🛒 ===============")
    print(f'{"PRODUTO":20} {"QTDE":>7} {"UNIDADE":>12} {"TOTAL":>12}')
    print("-" * 55)

    for item in carrinho:
        subtotal = item["Valor Unitário"] * item["Quantidade"]
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
    saldo = orcamento - total
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

    orcamento = ler_float("Quanto de grana você tem? 💵 R$ ")
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

        valor = ler_float("Quanto custa? R$ ")
        quantidade = ler_float("Quantos vai levar?: ")
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
