import psutil
import platform
import cpuinfo
import subprocess
import os
import nmap
import socket
import threading

dict_geral = {}

def get_all_data():
    global dict_geral
    
    while True:
        dict_geral.update(get_cpu_data())
        dict_geral.update(get_memory_data())
        dict_geral.update(get_disk_data())
        dict_geral.update(get_net_data())
        dict_geral['list_procs'] = get_process_data()
        dict_geral['interfaces'] = get_interfaces_info()

def get_subnet_data():
    global dict_geral
    
    while True:
        if ('ip_address' in dict_geral.keys()):
            dict_geral['subnet_data'] = get_ip_data(dict_geral['ip_address'])
        else:
            pass

def get_cpu_data():
    
    dict_cpu = {}
    
    info = cpuinfo.get_cpu_info()
    
    dict_cpu['brand'] = info['brand_raw'] 
    dict_cpu['arch'] = info['arch']
    dict_cpu['bits'] = info['bits']
    dict_cpu['cpu_freq_curr'] = psutil.cpu_freq().current
    dict_cpu['cpu_freq_max'] = psutil.cpu_freq().max
    dict_cpu['core_count_log'] = psutil.cpu_count()
    dict_cpu['core_count_phys'] = psutil.cpu_count(logical=False)
    dict_cpu['cpu_info'] = platform.processor()
    dict_cpu['proc_plat'] = platform.platform()
    dict_cpu['cpu_percent'] = psutil.cpu_percent()
    dict_cpu['cpu_percent_percpu'] = psutil.cpu_percent(percpu = True)
    
    return dict_cpu

def get_memory_data():
    dict_mem = {}
    
    mem = psutil.virtual_memory()
    dict_mem['mem_percent'] = mem.percent
    dict_mem['mem_total'] = mem.total
    dict_mem['mem_used'] = mem.used
    
    return dict_mem

def get_disk_data():
    
    dict_disk = {}
    
    d = psutil.disk_usage("C:")
    dict_disk['disk_used'] = d.used
    dict_disk['disk_total'] = d.total
    
    return dict_disk

def get_net_data():
    
    dict_net = {}
    
    dict_interfaces = psutil.net_if_addrs()
    
    dict_net['ip_address'] = dict_interfaces['Ethernet'][1].address
    
    return dict_net

def get_process_data():
    
    def memory_use(proc):
        return(proc['memory_percent'])
    
    lista_procs = []

    for proc in psutil.process_iter():
        
        lista_procs.append(proc.as_dict(attrs=['name', 'memory_percent', 'memory_info', 'pid']))

    lista_procs.sort(key = memory_use, reverse = True)

    return lista_procs[0:10]

def get_ip_data(ip):
    
    string_reply = ""
    
    ip_lista = ip.split(".")
    subrede = ".".join(ip_lista[0:3]) + "."
    
    string_reply += "Teste na subrede: {0}\n".format(subrede)
    hosts_validos = verifica_hosts(subrede)
    string_reply += obter_hostnames(hosts_validos) + "\n"
    string_reply += scan_hosts(hosts_validos)
    
    return string_reply

def retorna_codigo_ping(host):
    platforma = platform.system()
    if (platforma == "Windows"):
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", host]
    else:
        args = ["ping", "-c", "1", "-W", "1", host]
    cod_ret = subprocess.call(args, stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w"))
    return cod_ret

def verifica_hosts(subrede):
    hosts_validos = []
    for i in range(1, 5):
        ip = subrede + str(i)
        if (retorna_codigo_ping(ip) == 0):
            hosts_validos.append(ip)
    return hosts_validos

def obter_hostnames(host_validos):
    
    string_reply = ""
    
    nm = nmap.PortScanner()
    for host in host_validos:
        try:
            nm.scan(host)
            string_reply += "IP {0} possui o nome {1}".format(host, nm[host].hostname() if nm[host].hostname() != "" else host) + "\n"
        except:
            string_reply += "Erro no host {0}".format(host) + "\n"
    
    return string_reply

def scan_hosts(hosts_validos):
    
    string_reply = ""
    
    nm = nmap.PortScanner()
    for host in hosts_validos:
        nm.scan(host)
        if (nm[host].hostname() != ""):
            string_reply += "Nome do host: {0}".format(nm[host].hostname()) + "\n"
        else:
            string_reply += "Nome do host: {0}".format(host) + "\n"
        for proto in nm[host].all_protocols():
            string_reply += "Protocolo: {0}".format(proto) + "\n"
            lport = nm[host][proto].keys()
            for port in lport:
                string_reply += "\tPorta: {0} | Estado: {1}".format(port, nm[host][proto][port]["state"]) + "\n"
        string_reply += "\n"
    return string_reply

def get_interfaces_info():
    
    dict_net_address = psutil.net_if_addrs()
    dict_io_counters = psutil.net_io_counters(pernic=True)
    
    dict_interfaces = {}
    
    for nome in dict_net_address: #nome é a key, a key retorna uma lista de tupla nomeadas
        dict_dados = {}
        dict_dados['ip'] = dict_net_address[nome][1].address
        dict_dados['netmask'] = dict_net_address[nome][1].netmask
        dict_dados['bytes_sent'] = dict_io_counters[nome].bytes_sent
        dict_dados['bytes_recv'] = dict_io_counters[nome].bytes_recv
        dict_dados['packets_sent'] = dict_io_counters[nome].packets_sent
        dict_dados['packets_recv'] = dict_io_counters[nome].packets_recv
        
        dict_interfaces[nome] = dict_dados
    return dict_interfaces

