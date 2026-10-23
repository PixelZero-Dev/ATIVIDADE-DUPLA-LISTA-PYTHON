import os
os.system('cls')

# Desconto por quantidade no caixa - Atacarejo Bom Preço

print("=== Atacarejo Bom Preço - Cálculo de Desconto ===\n")

# Entrada de dados
produto = input("Nome do produto: ")
quantidade = int(input("Quantidade comprada: "))
preco_unitario = float(input("Preço unitário (R$): "))

# Cálculo do total sem desconto
total = quantidade * preco_unitario

# Define o percentual de desconto com if / elif / else
if quantidade <= 5:
    percentual = 2
elif quantidade <= 10:
    percentual = 3
else:
    percentual = 5

# Calcula o valor do desconto e o total a pagar
desconto = total * (percentual / 100)
total_pagar = total - desconto

# Exibe o resultado
print("\n========== RESUMO DA COMPRA ==========")
print(f"Produto: {produto}")
print(f"Total sem desconto: R$ {total:.2f}")
print(f"Desconto ({percentual}%): R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")
print("======================================")