"""
Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso. Exemplo:
"""

f = open("q3.txt", "r")
f_reversed = reversed(list(f))
string_reversed = ""

for linha in f_reversed:
    for c in reversed(linha):
        string_reversed += c

f.close()

print(string_reversed)