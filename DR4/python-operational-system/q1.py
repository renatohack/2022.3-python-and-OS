"""
Escreva um programa em Python que:
a) obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
b) imprima o nome do processo e seu PID;
c) imprima também o percentual de uso de CPU e de uso de memória.
"""

import psutil

for proc in psutil.process_iter():
    try:
        processo = psutil.Process(proc.pid)
        print("Nome: " + processo.name())
        print("PID: " + str(processo.pid))
        print("CPU Perc.: " + str(processo.cpu_percent()) + "%")
        print("Mem. Perc.: " + str(processo.memory_percent()) + "%")
        print()
    except:
        pass
        