"""
Escreva um programa cliente e servidor sobre UDP em Python que:
a) O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
b) O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.
"""

import socket 
import psutil

mysocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

mysocket.bind((socket.gethostname(), 8888)) 

while True:     
    pacote, dest = mysocket.recvfrom(1024)
    mem_total = str(round(psutil.virtual_memory().total / (2 ** 30), 2)) + " GB"
    mem_disp = str(round(psutil.virtual_memory().available / (2 ** 30), 2)) + " GB"
    msg = "Memória total: {0} | Memória disponível: {1}".format(mem_total, mem_disp)
    mysocket.sendto(msg.encode(), dest)

mysocket.close() 