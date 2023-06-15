
import socket
import sys
import os
import time
import copy
import datetime as dt
import threading
import queue
#from threading import Thread, currentThread

portnumber = 10001
#portnumber = 12348
data1 = ""
#input_command = "BBBB"
command = ""
new_client_address = ""
new_clientsocket = ""
#localhost = socket.gethostname()
#localhost = "192.168.0.102"
localhost = "192.168.11.132"

# 将全局使用的变量定义在类中        
class G:
    input_command = "BBBB"
    message_from_tower = " "
    

class Server:
    """ socket 服务端 """
    global input_command
    
    def __init__(self,port,host= localhost):
        self.port = port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind((host, self.port))
        self.msg = None
        self.new_command = None
        self.new_message = None
        self.already_sent = False
        
        print(f"the server IP is {host},{self.port}")

    def read(self, conn: socket.socket = None):
        """ 从tcp连接里面读取数据 """
        while True:
            try:
                data = conn.recv(1024).decode()
            except Exception as e:
                print("recv failed: %s", e)
                return
            print("[R %s]<< %s", threading.current_thread().ident, data)
            self.msg = data
            if self.msg == "photoyeye is blocking":
                G.message_from_tower = "photoyeye is blocking"
            if self.msg == "photoyeye is unblock":
                G.message_from_tower = "photoyeye is unblock"
            #time.sleep(1)

    def write(self, conn: socket.socket = None):
        """ 向tcp连接里面写入数据 """
        global input_command
        #global q
        while True:
            msg = f"{dt.datetime.now()} - {self.msg}"
            #print("[W %s]>> %s", threading.current_thread().ident, msg)
            try:
                #conn.send(msg.encode())

                #input_command=q.get()
                #print(f"{G.input_command}command sent to tower")
                if G.input_command != self.new_command: #and self.already_sent == False:
                    self.new_command = G.input_command
                    conn.send(self.new_command.encode())
                    print(f"{self.new_command}command sent to tower")
                    #self.already_sent = True
                if G.message_from_tower != self.new_message : #and self.already_sent == False:
                    self.new_message = G.message_from_tower
                    if self.new_message == "photoyeye is blocking":
                        conn.send(bytes(f"LED_ON","utf-8"))
                        print("LED_ON command sent to tower")
                    if self.new_message == "photoyeye is unblock":
                        conn.send(bytes(f"LED_OFF","utf-8"))
                        print("LED_OFF command sent to tower")

                #pass
            except Exception as e:
                print("send failed: %s", e)
                return
            #time.sleep(1)

    def serve(self):
        """ 开启服务 """
        self._sock.listen(5)
        print("Serving...")
        while True:
            print("Waiting for connection...")
            conn, addr = self._sock.accept()
            print("Recived new conn: %s from %s", conn, addr)
            # 开启读写线程处理当前连接
            threading.Thread(target=self.read, daemon=True,args=(conn, )).start()
            threading.Thread(target=self.write, daemon=True,args=(conn, )).start()

def get_input():
    #global input_command
    #global q
    while True:
        G.input_command = input()
        #q.put(input_command)
        print(f"Key input is {G.input_command}")

if __name__ == '__main__':

    #q=queue.Queue(1) 
    #localhost = socket.gethostname()
    server_to_tower1 = Server(10001)
    threading.Thread(target= server_to_tower1.serve , daemon=True).start()

    server_to_tower2 = Server(10002)
    threading.Thread(target= server_to_tower2.serve , daemon=True).start()

    input_thread = threading.Thread(target=get_input, daemon=True).start()

   
    #s.serve()

    while True:
        try:
            time.sleep(20)
            print(f"main thread of {threading.get_ident()} is alive.....")
            print(f"the pid is {os.getpid()}")
        except KeyboardInterrupt:
            print("you just pressed control + C, and it exited")
            exit()