import os
os.system("cls")

notas = []

for i in range(3):
    nota = float(input(f"Digite a {i + 1}ª nota: "))

    while nota < 0 or nota > 10:
        print("Nota inválida! Digite um valor entre 0 e 10.")
        nota = float(input(f"Digite a {i + 1}ª nota: "))

    notas.append(nota)

media = sum(notas) / 3

print(f"Média: {media:.1f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")