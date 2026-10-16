import os
os.system('cls')

vetor = []

match vetor:
    case 1:
        print('Muito frio')
    case 2:
        print('Frio')
    case 3:
        print('Agradável')
    case _:
        print('Muito quente')
