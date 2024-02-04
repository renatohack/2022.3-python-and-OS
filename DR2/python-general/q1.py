"""
Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.
"""
t = ()

for _ in range(3):
    t += (int(input("Entre com um número: ")),)

lista = list(t)
lista.sort()

for i in lista:
    print(i)









