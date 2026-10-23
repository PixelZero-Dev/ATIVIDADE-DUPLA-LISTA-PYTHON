import os
os.system('cls')

# Checkout: à vista ou a prazo - Mundo Eletro

print("=== Mundo Eletro - Checkout ===\n")

# Entrada de dados
valor = float(input("Valor do produto (R$): "))
forma = int(input("Forma de pagamento (1 - à vista / 2 - a prazo): "))

# Processamento com match-case + if
match forma:
    case 1:  # À vista
        desconto = valor * 0.10
        total = valor - desconto
        print("\n========== RESUMO DO PAGAMENTO ==========")
        print(f"Valor do produto: R$ {valor:.2f}")
        print(f"Forma de pagamento: À vista")
        print(f"Desconto (10%): R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
        print("=========================================")

    case 2:  # A prazo
        parcelas = int(input("Quantidade de parcelas (máximo 6): "))

        if parcelas < 1 or parcelas > 6:
            print("\nErro: o número de parcelas deve ser entre 1 e 6.")
        else:
            valor_parcela = valor / parcelas
            print("\n========== RESUMO DO PAGAMENTO ==========")
            print(f"Valor do produto: R$ {valor:.2f}")
            print(f"Forma de pagamento: A prazo")
            print(f"Parcelas: {parcelas}x de R$ {valor_parcela:.2f}")
            print(f"Total a pagar: R$ {valor:.2f}")
            print("=========================================")

    case _:
        print("\nOpção inválida! Digite 1 para à vista ou 2 para a prazo.")