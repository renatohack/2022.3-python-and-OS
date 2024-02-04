"""
Escreva um programa em Python que:
a) gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam em disco. Obtenha o nome do diretório do usuário.
b) Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
c) gere um arquivo texto com os valores desta estrutura ordenados.
"""

import os

dir = input("Entre com o caminho de um diretorio: ")
dict_files = {}

if (os.path.exists(dir) and os.path.isdir(dir)):
    lista_files = os.listdir(dir)
    for file in lista_files:
        file_abs = os.path.join(dir, file)
        if (os.path.isfile(file_abs)):
            dict_files[file] = os.stat(file_abs).st_size
    dict_sorted = dict(sorted(dict_files.items(),key= lambda x:x[1]))

    f = open("q3.txt", "w")

    for key, value in reversed(dict_sorted.items()):
        string_write = "{0}: {1}\n".format(key, value)
        f.write(string_write)
        
    f.close()
else: print("Diretório inválido.")