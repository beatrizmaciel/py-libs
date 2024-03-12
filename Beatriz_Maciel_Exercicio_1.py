# Faça um programa que utilize duas funções definidas por você.

a = int(input("Escreva um número inteiro: "))
b = int(input("Escreva outro número inteiro: "))

def soma(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

escolha = int(input("Você deseja somar? Digite 0. Deseja multiplicar? Digite 1 : "))

if(escolha == 0):
    print("O resultado da soma é: ", soma(a, b))
elif(escolha == 1):
    print("O resultado da multiplicação é: ", multiplicar(a, b))
else:
    print("Escolha 0 ou 1")