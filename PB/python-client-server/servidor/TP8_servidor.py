import socket 
import get_data_function_servidor, data_to_string
import threading
import os

"""
mysocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

mysocket.bind((socket.gethostname(), 8888)) 

while True:     
    pacote, dest = mysocket.recvfrom(1024)
    mem_total = str(round(psutil.virtual_memory().total / (2 ** 30), 2)) + " GB"
    mem_disp = str(round(psutil.virtual_memory().available / (2 ** 30), 2)) + " GB"
    msg = "Memória total: {0} | Memória disponível: {1}".format(mem_total, mem_disp)
    mysocket.sendto(msg.encode(), dest)
"""


# ** ---------------------------------------------------------------------------------------------------------

mysocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
mysocket.bind((socket.gethostname(), 8888)) 

# configuracao inicial da página
lista_opcoes = ["CPU info", "Memory info", "Disk info", "IP info", "Directory info", "Process info", "Subnet info", "Interfaces info"]
num_paginas = len(lista_opcoes)

# inicializa as threads usadas   
thread_get_data = threading.Thread(target=get_data_function_servidor.get_all_data, args=())
thread_get_data.start()
#wait dict to be initalized
while (not get_data_function_servidor.dict_geral):
    pass

thread_get_data = threading.Thread(target=get_data_function_servidor.get_subnet_data, args=())
thread_get_data.start()

while True: 
    codigo, dest = mysocket.recvfrom(1024)
    counter = int(codigo.decode())
    print(counter)
    
    pagina = counter % num_paginas
    opcao = lista_opcoes[pagina]
    
    msg_to_reply = data_to_string.get_string_data(opcao, get_data_function_servidor.dict_geral, pagina, num_paginas)
    os.system('cls')
    print(msg_to_reply)
    mysocket.sendto(msg_to_reply.encode(), dest)