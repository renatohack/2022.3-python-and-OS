from tabulate import tabulate
import os
import keyboard
import time
import sched
import get_data_functions


counter = 0

def update_counter():
    global counter
    
    while True:
        if (keyboard.is_pressed('right')):
            counter += 1
            time.sleep(0.2)
        elif(keyboard.is_pressed('left')):
            counter -= 1
            time.sleep(0.2)

def show_data(opcao, dict_geral, pagina, num_paginas):
    
    #limpa a tela e exibe o cabecalho
    os.system("cls")
    print("Página {0} / {1} - {2}".format(pagina + 1, num_paginas, opcao))

    if (opcao == "CPU info"):
        show_cpu_info(dict_geral)
    elif (opcao == "Memory info"):
        show_memory_info(dict_geral)
    elif (opcao == "Disk info"):
        show_disk_info(dict_geral)
    elif (opcao == "IP info"):
        show_net_info(dict_geral)
    elif (opcao == "Directory info"):
        print("Pressione BACKSPACE para indicar um diretório a ser analisado.")
        if (keyboard.is_pressed('backspace')):
            show_directory_info()
    elif (opcao == "Process info"):
        print("Pressione BACKSPACE para ver os 10 processos que mais estão consumindo memória.")
        if (keyboard.is_pressed('backspace')):
            list_procs = dict_geral['list_procs']
            show_process_info(list_procs)
    elif (opcao == "Subnet info"):
        print("Pressione BACKSPACE para analisar a subrede. Esse processo pode demorar alguns minutos.")
        if (keyboard.is_pressed('backspace')):
            show_ip_info()
    elif (opcao == "Interfaces info"):
        show_interfaces_info(dict_geral)

def show_memory_info(dict_mem):
    
    tabela_memoria = []
    header = ["MEMORY INFO"]
    tabela_memoria.append(header)
    
    int_perc = int(dict_mem['mem_percent'])
    round_total = round(dict_mem['mem_total'] / (1024 ** 3), 2)
    round_used = round(dict_mem['mem_used'] / (1024 ** 3), 2)
    
    str_mem_used = "Uso de Memória: {0} GB / {1} GB\n".format(round_used, round_total)
    str_mem_used += "[{0}{1}] {2}%".format("█" * int_perc, " " * (100 - int_perc), dict_mem['mem_percent'])
    tabela_memoria.append([str_mem_used])
    
    print(tabulate(tabela_memoria, headers = "firstrow", tablefmt="double_grid"))
    
    print()
    
def show_cpu_info(dict_cpu):
    
    tabela_cpu = []
    header = ["CPU INFO"]
    
    str_cpu_info = "{0} | {1}".format(dict_cpu['cpu_info'], dict_cpu['proc_plat'])
    
    str_tabela_info_geral = tabulate(generate_table_cpu(dict_cpu), headers="firstrow", tablefmt="simple")
    
    cpu_perc = dict_cpu['cpu_percent']
    int_perc = 1 if int(cpu_perc) < 1 else int(cpu_perc)
    str_cpu_usage = "Uso de CPU TOTAL:\n"
    str_cpu_usage += "[{0}{1}] {2}%\n\n".format("█" * int_perc, " " * (100 - int_perc), cpu_perc)
    
    # CPU USAGE EACH CORE
    for i in range(len(dict_cpu['cpu_percent_percpu'])):
    
        cpu_perc = dict_cpu['cpu_percent_percpu'][i]
        int_perc = 1 if int(cpu_perc) < 1 else int(cpu_perc)
        
        str_cpu_usage += "Uso de CPU {0}:\n".format(i + 1)
        str_cpu_usage += "[{0}{1}] {2}%\n\n".format("█" * int_perc, " " * (100 - int_perc), cpu_perc)
    
    tabela_cpu.append(header)
    tabela_cpu.append([str_cpu_info])
    tabela_cpu.append([str_tabela_info_geral])
    tabela_cpu.append([str_cpu_usage])
    
    print(tabulate(tabela_cpu, headers = "firstrow", tablefmt="double_grid"))    
    
    print()
    
def show_disk_info(dict_disk):

    tabela_disk = []
    header = ["DISK INFO"]
    
    
    int_perc = int((dict_disk['disk_used'] / dict_disk['disk_total']) * 100)
    round_total = round(dict_disk['disk_total'] / (1024 ** 3), 2)
    round_avail = round(dict_disk['disk_used'] / (1024 ** 3), 2)
    
    str_disk_used = "Uso de Disco: {0} GB / {1} GB\n".format(round_avail, round_total)
    str_disk_used += "[{0}{1}] {2}%".format("█" * int_perc, " " * (100 - int_perc), int_perc)
    
    tabela_disk.append(header)
    tabela_disk.append([str_disk_used])
    
    print(tabulate(tabela_disk, headers = "firstrow", tablefmt="double_grid")) 
    print()

def show_net_info(dict_net):
    
    tabela_net = []
    header = ["NET INFO"]
    str_ip_address = "Endreço IP: {0}".format(dict_net['ip_address'])
    
    tabela_net.append(header)
    tabela_net.append([str_ip_address])
    
    print(tabulate(tabela_net, headers = "firstrow", tablefmt="double_grid")) 

def generate_table_cpu(dict_cpu):
    # build table cpu
    tabela_cpu = []
    
    headers = ['Nome', 'Arch', 'Palavra (bits)', 'Freq. Atual (MHz)', 'Freq. Max (MHz)', 'Cores (fis.)', 'Cores (lóg.)']
    
    info_row = [dict_cpu['brand'],
                dict_cpu['arch'],
                dict_cpu['bits'],
                dict_cpu['cpu_freq_curr'],
                dict_cpu['cpu_freq_max'],
                dict_cpu['core_count_phys'],
                dict_cpu['core_count_log']]
    
    tabela_cpu.append(headers)
    tabela_cpu.append(info_row)
    
    return tabela_cpu

def show_directory_info():
    
    t_ini_total = time.time()
    t_ini_clock = time.process_time()
    
    directory = input("Entre com o caminho completo do diretório:")
    directory = directory.replace("\\", "/").replace("//", "/")
    
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0, 1, print_buscando, ("diretório", 1, 5))
    scheduler.run()
    time.sleep(5)
    
    if (os.path.exists(directory)):
        scheduler.enter(0, 2, print_dir_content, (directory,))
        scheduler.run()
    else:
        print("Esse diretório não existe.")
        
    t_fim_total = time.time()
    t_fim_clock = time.process_time()
    print("Tempo total decorrido: {0}".format(t_fim_total - t_ini_total))
    print("Tempo total de clocks: {0}".format(t_fim_clock - t_ini_clock))
    
    input("Aperte ENTER para prosseguir.")

def print_buscando(msg = "", interval = 0.5, iteracoes = 3):
    
    print("Buscando " + msg, end= "")
    for i in range(iteracoes):
        time.sleep(interval)
        print(".", end = "")
    print()

def print_dir_content(directory):
    lista = os.listdir(directory)
    tabela_dir = [["NOME", "TIPO", "TAMANHO (Bytes)"]]
    
    for i in lista:
        abs_path = directory + "/" + i
        if (os.path.isdir(abs_path)):
            tabela_dir.append([i, "Dir", ""])
        else:
            tabela_dir.append([i, "File", os.stat(abs_path).st_size])
            
    print(tabulate(tabela_dir, headers = "firstrow", tablefmt="double_grid"))

def show_process_info(list_procs):
    
    tabela_procs = [["TOP 10 MOST MEMORY CONSUMING PROCESSES"]]
    
    tabela_procs_ram = [["Nome", "Mem. %", "Mem. Used (MB)", 'PID']]

    for proc in list_procs:
        
        nome = proc["name"]
        mem_perc = round(proc["memory_percent"], 2)
        mem_used = round(proc["memory_info"].rss / (1024 ** 2), 2)
        pid = proc['pid']
        tabela_procs_ram.append([nome, mem_perc, mem_used, pid])
        
    tabela_procs.append([tabulate(tabela_procs_ram, headers = "firstrow", tablefmt="double_grid")])
    
    print(tabulate(tabela_procs, headers = "firstrow", tablefmt="double_grid"))
    
    input("Aperte ENTER para prosseguir.")

def show_ip_info():
    
    ip = input("Entre com o IP cuja subrede deve ser analisada: ")
    
    get_data_functions.get_ip_data(ip)
    
    input("Aperte ENTER para continuar")

def show_interfaces_info(dict_geral):
    
    dict_interfaces = dict_geral['interfaces']
    tabela_interface = []
    header = ['Interface', 'Endereço IP', "Máscara de Subrede", "Bytes Enviados", "Bytes Recebidos", "Pacotes Enviados", "Pacotes Recebidos"]
    tabela_interface.append(header)
    
    for nome in dict_interfaces: #retorna a key que é o nome da interface
        ip = dict_interfaces[nome]['ip']
        mascara = dict_interfaces[nome]['netmask']
        bytes_sent = dict_interfaces[nome]['bytes_sent']
        bytes_recv = dict_interfaces[nome]['bytes_recv']
        packets_sent = dict_interfaces[nome]['packets_sent']
        packets_recv = dict_interfaces[nome]['packets_recv']
        tabela_interface.append([nome, ip, mascara, bytes_sent, bytes_recv, packets_sent, packets_recv])
    
    print(tabulate(tabela_interface, headers = "firstrow", tablefmt="double_grid"))