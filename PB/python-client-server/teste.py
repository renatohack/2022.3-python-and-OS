from display_functions import *
from get_data_functions import *
import threading
import time
import nmap

nm = nmap.PortScanner()
nm.scan("192.168.15.4")
print(nm["192.168.15.4"].all_protocols())



