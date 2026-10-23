import os
os.system('cls')

# Pré-análise de empréstimo - Financeira Confia

print("=== Financeira Confia - Pré-análise de Crédito ===\n")

# Entrada de dados
renda = float(input("Renda mensal do cliente (R$): "))
valor_emprestimo = float(input("Valor do empréstimo pedido (R$): "))
num_prestacoes = int(input("Número de prestações: "))

# Calcula o valor da prestação
prestacao = valor_emprestimo / num_prestacoes

# Verifica as regras de aprovação
limite_emprestimo = renda * 10          # no máximo 10× a renda
limite_prestacao = renda * 0.30         # no máximo 30% da renda

# Análise com if / else
if valor_emprestimo <= limite_emprestimo and prestacao <= limite_prestacao:
    status = "APROVADO"
else:
    status = "NEGADO"

# Exibe o resultado
print("\n========== RESULTADO DA ANÁLISE ==========")
print(f"Valor da prestação: R$ {prestacao:.2f}")
print(f"Status do crédito: {status}")
print("==========================================")