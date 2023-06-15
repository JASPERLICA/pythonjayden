

import threading
import time
import os
class G:
    input_command = "BBBB"

def get_input():
    #global input_command
    #global q
    while True:
        G.input_command = input("type your words here")
        #q.put(input_command)
        print(f"Key input is {G.input_command}")

if __name__ == '__main__':

    input_thread = threading.Thread(target=get_input, daemon=True).start()

    while True:
        try:
            time.sleep(20)
            print(f"main thread of {threading.get_ident()} is alive.....")
            print(f"the pid is {os.getpid()}")
        except KeyboardInterrupt:
            print("you just pressed control + C, and it exited")
            exit()