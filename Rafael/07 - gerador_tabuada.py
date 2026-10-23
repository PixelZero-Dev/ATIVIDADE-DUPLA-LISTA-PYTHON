import os
import time
os.system('cls')

# Gerador de tabuada - Escola Aprender+
print("=== Escola Aprender+ - Gerador de Tabuada ===\n")

# Entrada do número
numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:\n")

# Laço for com range(1, 11)
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    time.sleep(1)  # Bônus: exibe uma linha por segundo