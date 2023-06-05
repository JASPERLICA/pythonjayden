import socket
import time
import threading
import os
# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
def task(hostname, port,taskdefine):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((hostname,port))
    s.listen(5)

    while True:
        
        # now our endpoint knows about the OTHER endpoint.
            print("this is threading number",taskdefine,threading.get_ident())
            clientsocket, address = s.accept()
            print(clientsocket)
            print(address)
            print(address[0])
            print(address[1])
            print(os.getpid())
            print(f"Connection from {address} has been established.")
            clientsocket.send(bytes(f"Hey there!!! your ip address and port are{address[0]},{address[1]}","utf-8"))
            clientsocket.send(b'This is byte by b')
            print('send out')
            time.sleep(0.1)
        #except KeyboardInterrupt:
        #   print("\nApplication exit!")

def main():
      
    #   name = socket.gethostname()
    #   port = 12345
    #   port1 = 12346
      name,port = (socket.gethostname(),12345)
      t = threading.Thread(target=task, args=(name,port,"t"))
      t.daemon = True
      t.start()
      #print("this is threading number",t.get_ident())
      name,port1 = (socket.gethostname(),12346)
      t1 = threading.Thread(target=task, args=(name,port1,"t1"))
      #print(os.getpid())
      t1.daemon = True
      t1.start()
      #print("this is threading number",t1.get_ident())

      while(True):
            try:
                print("this is while threading number",threading.get_ident())
                time.sleep(10)
                print("this is pid",os.getpid())
            except KeyboardInterrupt:
                  print("ctrl + C pressed,exit from main")
                  exit(0)

if __name__ == "__main__":
    main()
    print("exit from __main__")