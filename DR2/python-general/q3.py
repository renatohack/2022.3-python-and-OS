"""
Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B, e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação. Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.
"""

def potencia(base, expoente):
    
    produto = 1
    
    for _ in range(expoente):
        produto *= base
    return produto

base = int(input("Entre com a base: "))
expoente = int(input("Entre com o expoente: "))
print(potencia(base, expoente))






