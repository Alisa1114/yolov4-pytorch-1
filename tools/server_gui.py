# -*- coding: UTF-8 -*-
import socket
import threading
import tkinter as tk
import time
from PIL import Image, ImageTk
from playsound import playsound

window = tk.Tk()
row = 1

def notify_sound():
    playsound('tools/notify.mp3')

def show_message(message):
    global row
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
    label_time = tk.Label(window, text=result, fg='#263238', font=('Arial', 12), width=30, height=2)
    label_time.grid(column=0, row=row)
    
    label_message = tk.Label(window, text=message, fg='#263238', font=('Arial', 12), width=35, height=2)
    label_message.grid(column=1, row=row)
    
    t_notify = threading.Thread(target = notify_sound)
    t_notify.start()
    
    row += 1
    if row > 10:
        row = 1

def server():
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


def creat_label():
    label1 = tk.Label(window, text='日期與時間', bg='yellow', fg='#263238', font=('Arial', 12), width=30, height=2)
    label1.grid(column=0, row=0)
    label2 = tk.Label(window, text='地址', bg='orange', fg='#263238', font=('Arial', 12), width=35, height=2)
    label2.grid(column=1, row=0)

if __name__=='__main__':
    window.title('Window')
    window.geometry('980x710')
    creat_label()
    t_server = threading.Thread(target = server)
    t_server.daemon = True
    t_server.start()
    window.mainloop()