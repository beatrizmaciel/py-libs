# Faça três programas que utilizem módulos nativos do Python (três módulos deverão ser utilizados, 
# no mínimo, isto é, ao menos um módulo diferente em cada um dos programas).

import random

print("Escolha cinco números inteiros e receba-os numa ordem aleatória.")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
d = int(input("Digite o quarto número: "))
e = int(input("Digite o quinto número: "))

lista_de_numeros = [a, b, c, d, e]

random.shuffle(lista_de_numeros)

print("Sua ordem aleatória é: ", lista_de_numeros)