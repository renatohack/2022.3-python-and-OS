"""
Escreva um programa cliente e servidor sobre TCP em Python em que:
a) O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
b) O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
"""

# SERVIDOR - transferência de arquivos
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 8881))
sock.listen()

while True:
    print('aguardando conexao...')
    conexao, end_cliente = sock.accept()
    print("--------------------------")
    print("NOVA CONEXÃO: ", end_cliente)
    
    # avisa que o cliente se conectou
    conexao.send('Conectado.\n'.encode())
    
    # recebe o nome do arquivo que tem que ser transmitido e verifica se ele existe
    try:
        # pega o nome do arquivo
        nome_dir = conexao.recv(2048).decode()
        if (os.path.exists(nome_dir)):
            lista_dir = os.listdir(nome_dir)
            lista_files = []
            for file in lista_dir:
                file_abs = os.path.join(nome_dir, file)
                if (os.path.isfile(file_abs)):
                    lista_files.append(file)
            conexao.send(str(lista_files).encode())
        else:
            conexao.send("-1".encode())
    except Exception as e:
        print(e)
    
    conexao.close() # encerra a conexão