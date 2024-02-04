"""
Escreva um programa em Python que leia dois arquivos, a.txt e b.txt.
Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela. Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao segundo elemento de b.txt, e assim sucessivamente. Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.
"""

from operator import length_hint


f_a = open("a.txt", "r")
f_b = open("b.txt", "r")

list_num_a = []
list_num_b = []

for linha in f_a:
    numeros = linha.split(" ")
    for num in numeros:
        list_num_a.append(int(num))

for linha in f_b:
    numeros = linha.split(" ")
    for num in numeros:
        list_num_b.append(int(num))

print(list_num_a)
print(list_num_b)

f_a.close()
f_b.close()

lista_resultado = [0] * max(len(list_num_a), len(list_num_b))

for index in range(len(lista_resultado)):
    if(index < len(list_num_a)):
        lista_resultado[index] += list_num_a[index]
    if(index < len(list_num_b)):
        lista_resultado[index] += list_num_b[index]

print(lista_resultado)