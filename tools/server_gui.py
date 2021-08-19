# -*- coding: UTF-8 -*-
import socket
import threading
import tkinter as tk
import time
import queue
from PIL import Image, ImageTk
from playsound import playsound

window = tk.Tk()
message_queue = queue.Queue(maxsize=10)

def notify_sound():
    playsound('tools/notify.mp3')

def show_message(message):
    global message_queue
    temp_queue = queue.Queue(maxsize=10)
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
    
    if message_queue.full():
        message_queue.get()
        message_queue.put([result, message])
    else:
        message_queue.put([result, message])
        
    index = message_queue.qsize() + 1
    while not message_queue.empty():
        message_list = message_queue.get()
        temp_queue.put(message_list)
        
        label_time = tk.Label(window, text=message_list[0], fg='#263238', font=('Arial', 12), width=30, height=2)
        label_time.grid(column=0, row=index)
        
        label_message = tk.Label(window, text=message_list[1], fg='#263238', font=('Arial', 12), width=45, height=2)
        label_message.grid(column=1, row=index)
        
        index -= 1
    message_queue, temp_queue = temp_queue, message_queue
    
    t_notify = threading.Thread(target = notify_sound)
    t_notify.start()
    
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
    label2 = tk.Label(window, text='地址', bg='orange', fg='#263238', font=('Arial', 12), width=45, height=2)
    label2.grid(column=1, row=0)

if __name__=='__main__':
    window.title('Server')
    window.geometry('1130x710')
    creat_label()
    t_server = threading.Thread(target = server)
    t_server.daemon = True
    t_server.start()
    window.mainloop()