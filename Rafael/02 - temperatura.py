import os
os.system('cls')

# Algoritmo para registrar temperaturas da semana

# Dias da semana
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

# Vetor (lista) para armazenar as temperaturas
temperaturas = []

print("Digite a temperatura de cada dia da semana:\n")

# Lê as 7 temperaturas
for i in range(7):
    temp = float(input(f"Temperatura de {dias[i]}: "))
    temperaturas.append(temp)

# Calcula a média, maior e menor
media = sum(temperaturas) / len(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)

# Exibe os resultados
print("\n========== RESULTADOS ==========")
print("Temperaturas registradas:")
for i in range(7):
    print(f"{dias[i]}: {temperaturas[i]}°C")

print(f"\nMédia da semana: {media:.2f}°C")
print(f"Maior temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")