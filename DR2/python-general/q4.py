"""
Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa. Imprima o vetor no final. Use listas.
"""

lista_numeros = []

for _ in range(5):
    lista_numeros.append(int(input("Entre com um numero: ")))

lista_numeros.reverse()

print(lista_numeros)




