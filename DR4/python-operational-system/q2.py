"""
Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.
"""

import os
import psutil
import subprocess

arq = input("Entre com o caminho completo de um arquivo .txt: ")

if (os.path.exists(arq)):
    os.system(arq)