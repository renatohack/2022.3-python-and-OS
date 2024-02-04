"""
Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive. O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.
"""

i = int(input("Entre com um número inteiro: "))
soma = 0

for i in range(i + 1):
    if i % 2 == 0:
        soma += i
        
print("A soma dos numeros pares é", soma)









