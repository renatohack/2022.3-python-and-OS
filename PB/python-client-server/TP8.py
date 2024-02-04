import time, threading, display_functions, get_data_functions

# configuracao inicial da página
lista_opcoes = ["CPU info", "Memory info", "Disk info", "IP info", "Directory info", "Process info", "Subnet info", "Interfaces info"]
num_paginas = len(lista_opcoes)
pagina = display_functions.counter % num_paginas
opcao = lista_opcoes[pagina]

# inicializa as threads usadas   
thread_get_data = threading.Thread(target=get_data_functions.get_all_data, args=())
thread_get_data.start()
#wait dict to be initalized
while (not get_data_functions.dict_geral):
    pass

# start counter
thread_counter = threading.Thread(target=display_functions.update_counter, args=())
thread_counter.start()

counter_antigo = display_functions.counter

while (True):
    
    # define a opcao da vez, baseada no counter
    pagina = display_functions.counter % num_paginas
    opcao = lista_opcoes[pagina]
    display_functions.show_data(opcao, get_data_functions.dict_geral, pagina, num_paginas)
    
    i = 0
    while(counter_antigo == display_functions.counter and i < 50):
        time.sleep(0.01)
        i += 1
    counter_antigo = display_functions.counter
