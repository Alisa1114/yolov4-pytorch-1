# -*- coding: utf-8 -*-
import socket
from server_gui import show_message

# HOST = '120.126.151.182' #實驗室電腦
# PORT = 8887

#在自己電腦測試的話
HOST = '127.0.0.1' 
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    conn, addr = s.accept()
    print('connected by ' + str(addr))

    while True:
        indata = conn.recv(1024)
        if len(indata) == 0: # connection closed
            conn.close()
            print('client closed connection.')
            break
        message = indata.decode()
        print('recv: ' + message)
        
        # 將傳來的訊息顯示在GUI視窗上
        show_message(message=message)

        outdata = 'echo ' + indata.decode()
        conn.send(outdata.encode())
