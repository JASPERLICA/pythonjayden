import socket
import sys
import threading
import os
import time
import copy
portnumber = 10001
#portnumber = 12348
data1 = ""
input_command = ""
def socket_set(portn,threadname):
    data1 = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), portn))
    print(f"there threadname is :{threadname}, and the thread ID is {threading.get_ident()}")
    print(os.getpid())
    s.listen(5)
    clientsocket,client_address = s.accept()
    print(f" {client_address} Client access server")
    clientsocket.send(bytes("server accept your connection","utf-8"))
    while True:
        data = clientsocket.recv(1024)
        print(data,"original data \n")
        print(data.decode(),"data \n")
        if data1 != data:
            data1 = copy.copy(data)
            print(data1.decode(),"data1 \n")
            
            if data1.decode() == "photoyeye is blocking":
                clientsocket.send(data)
        if data.decode() == "":
            print("bodyguard client disconnected so socket thread exit")
            exit()
            
def get_input():
    global input_command
    input_command = input()
    print(input_command)
    #return input_command




def main():
    t0 = threading.Thread(target = socket_set, args = (portnumber,"t0"))
    t0.daemon = True
    t0.start()

    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()

    while True:
        try:
            #  match input_command:
            #     case 400:
            #         return "Bad request"
            #     case 404:
            #         return "Not found"
            #     case 418:
            #         return "I'm a teapot"

            time.sleep(2)
            print(f"Mother thread of {threading.get_ident()} is alive.....")
            print(f"the pid is {os.getpid()}")
        except KeyboardInterrupt:
            print("you just pressed control + C, and it exited")
            exit()
if __name__ == "__main__":
    main()