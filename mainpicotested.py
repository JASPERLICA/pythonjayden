# This is the Bodyguard code on Pico only for hardward testing
#In the test,I found that the Raspberry Pi Pico does not have an operating system 
#that manages the CPU cycles and therefore it only allows one thread per core, 
#which in this case is two. one is the bodyguard_tower_receiver, another is main

try:
    import usocket as socket
except:
    import socket
from machine import Pin,SPI
from sys import exit
import urequests
import network
import time
import _thread

#define a global variable
thread_receiver_alive_flag = False
#server_IP = "192.168.0.102" #server running on my laptop
server_IP = "192.168.11.132" # server running on my computer at banalogic
# Bodyguard Pinout definition

led_panel = Pin(1, Pin.OUT,value = 1)
#led_panel.value(True)
upper_camera_trigger = Pin(7, Pin.IN, Pin.PULL_UP)
front_camera_trigger = Pin(8, Pin.IN, Pin.PULL_UP)
rear_camera_trigger = Pin(9, Pin.IN, Pin.PULL_UP)
photoeye_npn = Pin(10, Pin.IN, Pin.PULL_UP)
photoeye_pnp = Pin(5, Pin.IN, Pin.PULL_UP)
led_indicator = Pin(25, Pin.OUT)

portnumber = 10001

# Bodyguard tower DHCP configuration
def w5100_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)
#None DHCP
    #nic.ifconfig(('192.168.11.15','255.255.255.0','192.168.11.1','8.8.8.8'))
#DHCP
    nic.ifconfig('dhcp')
      
    print('IP address :', nic.ifconfig())
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
      
def bodyguard_client():
    s = socket.socket()
    s.connect((server_IP, portnumber))#10001 as fastlign
    print("bodyguard tower connected...")
    full_msg = ''
    while True:
            msg1 = s.recv(1024)
            if len(msg1) <= 0:
                break
            full_msg += msg1.decode("utf-8")
            print(full_msg)
            s.send(bytes(f"bodyguard tower received {full_msg} ","utf-8"))
            
def bodyguard_tower_receiver(s,):

    global thread_receiver_alive_flag
    while True:
        try:
            msg_data = s.recv(128)
            msg = msg_data.decode("utf-8")
            if msg == "":
                break
            if len(msg) <= 0:
                break
            if msg == "LED ON" or msg == "led on":
                led_panel.value(False) #ON
            if msg == "LED OFF" or msg == "led off":
                led_panel.value(True) #OFF
                     
            print(msg)
            s.send(bytes(f"bodyguard tower have received {msg} ","utf-8"))
        except OSError:
            print("Bodyguard server disconnected,recever thread exit")
            thread_receiver_alive_flag = True
            exit()
            

def main():
    
    global thread_receiver_alive_flag
    led_panel.value(True)
    
    w5100_init()  

    s = socket.socket()
    s.connect((server_IP, portnumber))#10001
    print("bodyguard tower connected...")
    
    _thread.start_new_thread(bodyguard_tower_receiver,(s,))
    
    time_update_time = time.time()
    time0 = time.time()
    toggle =  True
    photoeye_unsend = True
    time_upper_update_time = time.time()
    upper_unsend = True
    time_front_update_time = time.time()
    front_unsend = True
    time_rear_update_time = time.time()
    rear_unsend = True

    while True:  
        if photoeye_npn.value() is 0:
            if photoeye_unsend == True:
                s.send(bytes("photoyeye is blocking","utf-8"))
                print("photoyeye is blocking")
                photoeye_unsend = False
                time_update_time = time.time()
        else:
            if photoeye_unsend == False:
                if time.time() - time_update_time >= 1:
                    photoeye_unsend = True
                    s.send(bytes("photoyeye is unblock","utf-8"))
                    print("photoyeye is unblock")
              
              
        if upper_camera_trigger.value() == 1:
            if upper_unsend == True:
                s.send(bytes("upper_camera_trigger is tripped","utf-8"))
                print("upper camera is triggered")
                upper_unsend = False
                time_upper_update_time = time.time()
        else:
            if upper_unsend == False:
                if time.time() - time_upper_update_time >= 1:
                    upper_unsend = True
                    s.send(bytes("upper_camera_trigger is released","utf-8"))
                    print("upper_camera_trigger is released")
        
        if front_camera_trigger.value() == 1:
            if front_unsend == True:
                s.send(bytes("front_camera_trigger is tripped","utf-8"))
                print("front_camera_trigger is triggered")
                front_unsend = False
                time_front_update_time = time.time()
        else:
            if front_unsend == False:
                if time.time() - time_front_update_time >= 1:
                    front_unsend = True
                    s.send(bytes("front_camera_trigger is released","utf-8"))
                    print("front_camera_trigger is released")

        if rear_camera_trigger.value() == 1:
            if rear_unsend == True:
                s.send(bytes("rear_camera_trigger is tripped","utf-8"))
                print("rear_camera_trigger is triggered")
                rear_unsend = False
                time_rear_update_time = time.time()
        else:
            if rear_unsend == False:
                if time.time() - time_rear_update_time >= 1:
                    rear_unsend = True
                    s.send(bytes("rear_camera_trigger is released","utf-8"))
                    print("rear_camera_trigger is released")

        if thread_receiver_alive_flag == True:
            print("main thread exit....")
            exit()
        if time.time()- time0 >= 1:
            time0 = time.time()
            toggle = not toggle
            led_indicator.value(toggle)
            print("tower is alive...")
      
            
    
if __name__ == "__main__":
    main()
