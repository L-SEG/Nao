# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import socket
import threading
import time
from MoveAction import *
from HeadAction import *
from GestureReaction  import *
Nao_One = "192.168.1.106"
Nao_Two = "192.168.1.103"
Nao_Four = "192.168.1.109"
Nao_Five = "192.168.1.107"

robotIP = Nao_Four
PORT = 9559
def tcp_link(sock, addr,tts,motionProxy,postureProxy):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')

    while True:
        data = sock.recv(65535)
        time.sleep(1)
        if data=="1":
            print 'Ready to introduce'
            # Wake up robot
            motionProxy.wakeUp()
            # Send robot to Stand Init
            postureProxy.goToPosture("StandInit", 0.5)
            tts.say("尊敬的各位领导你们好，欢迎来到山东大学工程训练中心")

        elif data=="2":
            print  "Ready to TurnLeft"
            # tts.say("我由SDU-NAO创客团队开发")
            MoveAction_TurnLeft(robotIP, PORT=9559)
        elif data=="3":
            print  "Ready to MoveFOrward"
            # Go to rest position
            # MoveAction_1(robotIP, PORT=9559)
            MoveAction_MoveFor(robotIP, PORT=9559)

        elif data=="4":
            print data
            tts.say("山东大学工程训练中心坚持立足山大，服务山东，面向全国，示范辐射的服务宗旨，现已成为面向全校大学生的通识、实践、创新、教育基地，社会服务基地，按照确立一个目标，构建两个体系，加强三个建设，发挥四个功能的发展思路，致力于打造优质高效的综合性多功能创新实践教育平台")
        elif data=="5":
            print "Ready to TurnRight"
            # HeadAction(robotIP,PORT)    #躲子弹
            MoveAction_TurnRight(robotIP, PORT=9559)   #右转
        elif data=="6":
            print "Ready to Backward"
            MoveAction_Backward(robotIP, PORT=9559)    #后退
        if not data or data == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 6688))
s.listen(5)
tts1 = ALProxy("ALTextToSpeech", robotIP, PORT)
tts1.setLanguage("Chinese")
motionProxy1 = ALProxy("ALMotion", robotIP, PORT)
postureProxy1 = ALProxy("ALRobotPosture", robotIP, PORT)

while True:
    print "Tcp server connected！"
    sock, addr = s.accept()
    t = threading.Thread(target=tcp_link, args=(sock, addr,tts1,motionProxy1,postureProxy1))
    t.start()




