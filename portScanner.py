import socket
import threading
from queue import Queue

target = 'TARGET IP'
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
# print(portscan(80))

# for port in range(0, 1024):
#     result = portscan(port)
#     if result:
#         print(f'Port {port} is open')
#     else:
#         print(f'Port is closed {port}')

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f'Port {port} is open')
            open_ports.append(port)

port_list = range(1, 50)
fill_queue(port_list)        

thread_list = []

for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print('Open ports are', open_ports)