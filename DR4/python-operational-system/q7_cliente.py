"""
Escreva um programa cliente e servidor sobre UDP em Python que:
a) O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
b) O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.
"""

import socket 

mysocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

mysocket.settimeout(5) 

# PASSO 3: já começa a enviar mensagens ("pacotes")...
dest = (socket.gethostname(), 8888)  # endereço do servidor

info_received = False
counter = 0


while not info_received and counter < 5:  
    mysocket.sendto("1".encode(), dest)        
    try:          
        msg, address = mysocket.recvfrom(1024)             
        info_received = True         
    except socket.timeout:
        counter += 1

if(info_received): print (msg.decode())
else: print("Timeout na requisição.") 

mysocket.close() 