# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import socket
import threading
import time

def tcp_link(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')

    while True:
        data = sock.recv(65535)
        time.sleep(1)
        if data=="1":
            print 'hello'
            # tts.say("你好，我是NAO，我来自山东大学工程训练中心")
        elif data=="2":
            print  "world"
        elif data=="3":
            print data
            print "This is my first Word!"
        elif data == "4":
            print data
            print "This is my second Word!"

        if not data or data == 'exit':           ##
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 6688))
s.listen(5)

while True:
    print "ready for connection"
    sock, addr = s.accept()
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.start()




