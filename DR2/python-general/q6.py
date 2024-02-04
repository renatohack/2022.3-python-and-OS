"""
Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista contendo somente os números ímpares e uma nova tupla contendo somente os elementos nas posições pares.
"""

def separa_tupla(tupla):
    
    lista_impares = []
    tupla_posicoes_pares = ()
    
    for i in range(len(tupla)):
        if i % 2 == 0:
            tupla_posicoes_pares += (tupla[i],)
        if tupla[i] % 2 == 1:
            lista_impares.append(tupla[i])
    
    return lista_impares, tupla_posicoes_pares

print(separa_tupla((1, 2, 3, 4, 6, 7, 8, 9, 11)))




