import socket 
import util_functions
import threading
import time
import os

mysocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

dest = (socket.gethostname(), 8888) 


# start counter
thread_counter = threading.Thread(target=util_functions.update_counter, args=())
thread_counter.start()

counter_antigo = util_functions.counter


while True:  
    mysocket.sendto(str(counter_antigo).encode(), dest)
    msg, address = mysocket.recvfrom(40096)
    os.system('cls')
    print(msg.decode())
    
    i = 0
    while(counter_antigo == util_functions.counter and i < 100):
        time.sleep(0.01)
        i += 1
    counter_antigo = util_functions.counter