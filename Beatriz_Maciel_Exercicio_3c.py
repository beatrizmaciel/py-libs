# Faça três programas que utilizem módulos nativos do Python (três módulos deverão ser utilizados, 
# no mínimo, isto é, ao menos um módulo diferente em cada um dos programas).

import datetime

escolha = input("Deseja saber data e hora atuais? Digite y em caso afirmativo: ")

if(escolha == "y"):
    data_hora_atual = datetime.datetime.now()

    print("Data e hora atuais:", data_hora_atual)
else:
    print("Programa encerrado.")