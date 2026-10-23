import os
os.system("cls")

login_correto = input("Cadastre seu login: ")
senha_correta = input("Cadastre sua senha: ")

print("\n" * 50)

tentativas = 0
acesso = False

while tentativas < 3:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == login_correto and senha == senha_correta:
        print("Bem-vindo(a)! Acesso autorizado.")
        acesso = True
        break
    else:
        tentativas += 1
        print("Login ou senha incorretos!")

        if tentativas < 3:
            print(f"Tentativas restantes: {3 - tentativas}")

if not acesso:
    print("Acesso bloqueado. Número máximo de tentativas excedido.")