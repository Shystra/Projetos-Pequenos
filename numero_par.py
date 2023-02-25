# Faça um programa que peça ao usuário para digitar um número inteiro.
#Informe se o número é par ou impar. 

Entrada = int(input("Digite um número: "))

if Entrada.isdigit():
    entrada_int = int(Entrada)
    par_impar = Entrada % 2 == 0
    print(f'O numero {entrada_int} é {Entrada}')
else:
    print("Você não digitou um número inteiro")




