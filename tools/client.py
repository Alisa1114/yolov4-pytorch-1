from socket import *

def client():
    serverip='120.126.151.182' #實驗室電腦
    serverport=8887
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
    client.send(buffer.encode())
    print(client.recv(1024).decode())