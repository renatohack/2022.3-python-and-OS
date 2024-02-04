from tabulate import tabulate
import os
import keyboard
import time
import sched
import get_data_function_servidor

string_reply = ""

def get_string_data(opcao, dict_geral, pagina, num_paginas):
    
    global string_reply
    string_reply = ""
    
    string_reply += "Página {0} / {1} - {2}\n".format(pagina + 1, num_paginas, opcao)

    if (opcao == "CPU info"):
        string_reply += show_cpu_info(dict_geral)
    elif (opcao == "Memory info"):
        string_reply += show_memory_info(dict_geral)
    elif (opcao == "Disk info"):
        string_reply += show_disk_info(dict_geral)
    elif (opcao == "IP info"):
        string_reply += show_net_info(dict_geral)
    elif (opcao == "Directory info"):
        show_directory_info()
    elif (opcao == "Process info"):
        list_procs = dict_geral['list_procs']
        string_reply += show_process_info(list_procs)
    elif (opcao == "Subnet info"):
        string_reply += dict_geral['subnet_data'] if 'subnet_data' in dict_geral.keys() else "Ainda não há dados da subrede."
    elif (opcao == "Interfaces info"):
        string_reply += show_interfaces_info(dict_geral)
    
    return string_reply

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
    
    return tabulate(tabela_memoria, headers = "firstrow", tablefmt="double_grid")
    
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
    
    return tabulate(tabela_cpu, headers = "firstrow", tablefmt="double_grid")
    
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
    
    return tabulate(tabela_disk, headers = "firstrow", tablefmt="double_grid")

def show_net_info(dict_net):
    
    tabela_net = []
    header = ["NET INFO"]
    str_ip_address = "Endreço IP: {0}".format(dict_net['ip_address'])
    
    tabela_net.append(header)
    tabela_net.append([str_ip_address])
    
    return tabulate(tabela_net, headers = "firstrow", tablefmt="double_grid")

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
    
    global string_reply
    
    t_ini_total = time.time()
    t_ini_clock = time.process_time()
    
    directory = os.getcwd()
    directory = directory.replace("\\", "/").replace("//", "/")
    
    scheduler = sched.scheduler(time.time, time.sleep)

    if (os.path.exists(directory)):
        scheduler.enter(0, 2, print_dir_content, (directory,))
        scheduler.run()
    else:
        string_reply += "Esse diretório não existe.\n"
        return
    
    t_fim_total = time.time()
    t_fim_clock = time.process_time()
    string_reply += "Tempo total decorrido: {0}\n".format(t_fim_total - t_ini_total)
    string_reply += "Tempo total de clocks: {0}\n".format(t_fim_clock - t_ini_clock)

def print_dir_content(directory):
    global string_reply
    
    lista = os.listdir(directory)
    tabela_dir = [["NOME", "TIPO", "TAMANHO (Bytes)"]]
    
    for i in lista:
        abs_path = directory + "/" + i
        if (os.path.isdir(abs_path)):
            tabela_dir.append([i, "Dir", ""])
        else:
            tabela_dir.append([i, "File", os.stat(abs_path).st_size])
            
    string_reply += tabulate(tabela_dir, headers = "firstrow", tablefmt="double_grid") + "\n"

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
    
    return tabulate(tabela_procs, headers = "firstrow", tablefmt="double_grid")

def show_ip_info(ip):
    
    return get_data_function_servidor.get_ip_data(ip)

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
    
    return tabulate(tabela_interface, headers = "firstrow", tablefmt="double_grid")