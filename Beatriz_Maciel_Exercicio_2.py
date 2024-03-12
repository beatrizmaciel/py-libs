#  Escreva um programa Python para remover duplicatas de uma lista.

lista_de_alunos = [
    "João", "Sophie", "Ahmed", 
    "Sophie", "Li Wei", "Li Wei", 
    "Alejandro", "Priya", "Amir", "Amir"
]

print("A lista original é: ", lista_de_alunos, "e tem ", len(lista_de_alunos), " alunos.")

list_atualizada = []

for item in lista_de_alunos:
    if item not in list_atualizada:
        list_atualizada.append(item)

print("A lista sem duplicatas é: ", list_atualizada, "e tem ", len(list_atualizada), " alunos.")