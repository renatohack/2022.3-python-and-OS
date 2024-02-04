"""
Escreva 3 programas em Python que resolva o seguinte problema:
Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B.
"""
import random, time, threading, multiprocessing

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def calcFatorialThread(list_numeros, list_resultado, inicio, fim):
    for i in range(inicio, fim):
        list_resultado[i] = fatorial(list_numeros[i])

def calcFatorialMultiProc(q1, q2):
    
    lista_fat = q1.get()
    
    for x in range(len(lista_fat)):
        lista_fat[x] = (lista_fat[x], fatorial(lista_fat[x]))
    
    q2.put(lista_fat)

if __name__ == "__main__":
    
    numero_itens = (1_000_000, 5_000_000, 10_000_000)
    
    num_parts = 4

    for N in numero_itens:
        
        lista_numeros_raw = []
        for e in range(N):
            lista_numeros_raw.append(random.randint(1, 10))
        
        # SEQUENCIAL
        lista_fat_seq = [0] * N
        time_ini_seq = time.time()
        for i in range(len(lista_numeros_raw)):
            lista_fat_seq[i] = fatorial(lista_numeros_raw[i])
        time_final_seq = time.time()
        print("Tempo de processamento sequencial para {0} itens: {1}".format(N, time_final_seq - time_ini_seq))
        

        # THREAD
        time_ini = time.time()
        lista_fat_thread = [0] * N  
        Nthreads = num_parts

        lista_threads = []
        for i in range(Nthreads):
            ini = i * int(N / Nthreads) # início do intervalo da lista
            fim = (i + 1) * int(N / Nthreads) # fim do intervalo da lista
            t = threading.Thread(target=calcFatorialThread, args=(lista_numeros_raw, lista_fat_thread, ini, fim))
            t.start() # inicia thread
            lista_threads.append(t) # guarda a thread

        for t in lista_threads: t.join()

        time_final = time.time()
        print("Tempo de processamento em thread para {0} itens: {1}".format(N, time_final - time_ini))
        
        
        # MULTIPROCESSING
        time_ini = time.time()
        lista_fat_multiproc = []
        NProcs = num_parts
        
        q_entrada = multiprocessing.Queue()
        q_saida = multiprocessing.Queue()
        
        lista_procs = []
        for i in range(NProcs):
            ini = i * int(N/NProcs)       
            fim = (i + 1) * int(N/NProcs) 
            q_entrada.put(lista_numeros_raw[ini:fim]) 
            p = multiprocessing.Process(target=calcFatorialMultiProc, args=(q_entrada, q_saida))
            p.start()
            lista_procs.append(p)
        
        #for p in lista_procs: p.join()
        
        lista_fat_multiproc = []
        for i in range(NProcs):
            lista_fat_multiproc = lista_fat_multiproc + q_saida.get()
        
        
        time_final = float(time.time())
        print("Tempo de processamento em multiprocessamento para {0} itens: {1}".format(N, time_final - time_ini))

        
""""
No meu computador, para 4 thread e 4 multiprocess, os tempos são t_mult < t_thread < t_seq; com muito pouca diferença entre eles.
Porém, aumentando o número de thread e multiprocesses para 100, os resultados explodem, ficando como            t_thread < t_seq <<< t_mult.
"""
