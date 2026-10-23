import os
os.system("cls")

pares = 0
impares = 0
soma = 0

for i in range(5):
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    soma += numero

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
print("Soma dos números:", soma)