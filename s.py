import socket
import threading
import os
import time

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("\t\t\t\t------------------------------")
print("\t\t\t\t########## Chat App ##########")
print("\t\t\t\t------------------------------")
os.system('tput setaf 5')
serverip = input("\n\t\tEnter Your IP : ")
serverport = 8753

clientip = input("\n\t\tEnter Your Friends IP : ")
clientport = 8753

s.bind( (serverip, serverport) )

def send():
    while True:
        os.system('tput setaf 2')
        msg = input("Your Message: ").encode()
        s.sendto(msg,(clientip,clientport))
        if msg.decode() == "exit" or msg.decode() == "quit":
            os._exit(1)

def recv():
    while True:
        msg = s.recvfrom(1024)
        os.system('tput setaf 6')
        if msg[0].decode() == "quit" or msg[0].decode() == "exit":
            os._exit(1)
        print('\n\t\t\t\t\t\tReceived Msg: '+ msg[0].decode())
        


t1 = threading.Thread(target=recv)
t1.start()
    
t2 = threading.Thread(target=send)
t2.start()




