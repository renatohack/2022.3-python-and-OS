import os

path = "D:\\Users\\Renat\\OneDrive\\Área de Trabalho\\FACULDADE INFNET\\AULAS\\2022.2 - Python e Redes\\04 - Python SO e Redes\\TP5 - AT"

path = path.replace("\\", "/")

lista_dir = os.listdir(path)

for file in lista_dir:
    if (os.path.isfile(file)): print("FILE")
    else: print("ARQUIVO")