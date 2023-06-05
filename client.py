

import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 12345))
print('pid:',os.getpid())
msg = s.recv(80)
print(msg)
print('')
print(msg.decode())