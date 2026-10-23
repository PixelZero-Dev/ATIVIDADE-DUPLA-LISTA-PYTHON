import os
os.system('cls')


# Calculadora para os atendentes da CrediFácil usando match-case

print("=== Calculadora CrediFácil ===\n")

# Solicita os dois números e o operador
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, * ou /): ").strip()

# Usa match-case para escolher a operação
match operador:
    case "+":
        resultado = num1 + num2
        print(f"\n{num1} + {num2} = {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"\n{num1} - {num2} = {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"\n{num1} * {num2} = {resultado}")
    case "/":
        if num2 == 0:
            print("\nErro: divisão por zero não é permitida!")
        else:
            resultado = num1 / num2
            print(f"\n{num1} / {num2} = {resultado}")
    case _:
        print("\nOperador inválido! Use apenas +, -, * ou /.")