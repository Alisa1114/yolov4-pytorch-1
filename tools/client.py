# -*- coding: UTF-8 -*-
from socket import *

def client():
    #實驗室電腦
    # serverip='120.126.151.182' 
    # serverport=8887
    
    #在自己電腦測試
    serverip='127.0.0.1'
    serverport=8888
    
    client=socket(AF_INET,SOCK_STREAM)
    client.connect((serverip,serverport))
    
    buffer='POST /post HTTP/1.1\r\n'
    buffer+='Content-Type:application/json\r\n'
    address_file = open('tools/address.txt', 'r')
    address = address_file.read()
    #buffer+='Body:{\\"StuId\\":\\"410785016 Chao,He-Teng\\"}\r\n'
    buffer+='Address : ' + address + '\r\n'
    buffer+='\r\n'
    #print(buffer)
    message = "國立台北大學世界第一:)"
    client.send(message.encode())
    print(client.recv(1024).decode())
client()