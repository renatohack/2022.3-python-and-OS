"""
Escreva um programa cliente e servidor sobre TCP em Python em que:
a) O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
b) O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
"""

# CLIENTE - transferência de arquivos
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 8881))

# avisando que foi conectado ao servidor
msg_conexao = sock.recv(100).decode()
print(msg_conexao)

# pede para o cliente digitar o nome do arquivo
nome_dir = input('Qual o diretório que você deseja analisar? ')
sock.send(nome_dir.encode())

# recebe o tamanho do arquivou ou -1 se o arquivo não foi encontrado
lista_files = sock.recv(4096).decode()

if (lista_files != -1):
    print(lista_files)
else:
    print("Arquivo não encontrado no servidor.")
