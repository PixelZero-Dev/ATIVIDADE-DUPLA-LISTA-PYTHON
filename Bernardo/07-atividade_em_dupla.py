import os
os.system("cls")

quantidade = 0
total = 0

while True:
    print("\n===== RESTAURANTE SABOR DA TERRA =====")
    print("1 - Pizza       - R$ 35.00")
    print("2 - Hambúrguer  - R$ 25.00")
    print("3 - Lasanha     - R$ 30.00")
    print("4 - Salada      - R$ 18.00")
    print("5 - Macarrão    - R$ 22.00")

    codigo = int(input("Digite o código do prato: "))

    match codigo:
        case 1:
            prato = "Pizza"
            preco = 35.00
        case 2:
            prato = "Hambúrguer"
            preco = 25.00
        case 3:
            prato = "Lasanha"
            preco = 30.00
        case 4:
            prato = "Salada"
            preco = 18.00
        case 5:
            prato = "Macarrão"
            preco = 22.00
        case _:
            print("Código inválido!")
            continue

    print(f"Prato escolhido: {prato}")
    print(f"Preço: R$ {preco:.2f}")

    quantidade += 1
    total += preco

    resposta = input("Deseja outro prato? (S/N): ").strip().upper()

    while resposta not in ("S", "N"):
        resposta = input("Resposta inválida! Deseja outro prato? (S/N): ").strip().upper()

    if resposta == "N":
        break

print("\n===== RESUMO DO PEDIDO =====")
print(f"Quantidade de pratos: {quantidade}")
print(f"Total a pagar: R$ {total:.2f}")
print("Obrigado pela preferência!")