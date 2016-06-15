# -*- encoding: UTF-8 -*-

''' setFootStep: Small example to make Nao execute     '''
'''              The Cha Cha Basic Steps for Men       '''
'''              Using setFootStep API                 '''
''' http://www.dancing4beginners.com/cha-cha-steps.htm '''
''' This example is only compatible with NAO '''

import argparse
from naoqi import ALProxy
import threading

Nao_One = "192.168.1.106"
Nao_Two = "192.168.1.103"
Nao_Four = "192.168.1.109"
Nao_Five = "192.168.1.107"
lock=False
robotIP2 = Nao_One
robotIP3 = Nao_Four


def main(robotIP, PORT=9559):


    motionProxy1 = ALProxy("ALMotion", robotIP2, PORT)
    postureProxy1 = ALProxy("ALRobotPosture", robotIP2, PORT)
    motionProxy2 = ALProxy("ALMotion", robotIP3, PORT)
    postureProxy2 = ALProxy("ALRobotPosture", robotIP3, PORT)
    tts1 = ALProxy("ALTextToSpeech",Nao_Two , 9559)
    tts1.setLanguage("Chinese")

    # motion = ALProxy("ALMotion","192.168.0.102",9559)
    # motion .moveInit()
    # id  = motion .post.moveTo(0.5,-0.5,0)
    # motion.wait(id,0)
    # tts.post.say("你好，我是NAO，我来自山东大学工程训练中心")

    # Wake up robot
    #motionProxy.post.wakeUp()
    motionProxy1.post.wakeUp()
    motionProxy2.wakeUp()

    # Send robot to Stand Init
    #postureProxy.post.goToPosture("StandInit", 0.5)
    postureProxy1.post.goToPosture("StandInit", 0.5)
    postureProxy2.goToPosture("StandInit", 0.5)

    ###############################
    # First we defined each step
    ###############################
    footStepsList = []

    # 1) Step forward with your left foot
    footStepsList.append([["LLeg"], [[0.06, 0.1, 0.0]]])

    # 2) Sidestep to the left with your left foot
    footStepsList.append([["LLeg"], [[0.00, 0.16, 0.0]]])

    # 3) Move your right foot to your left foot
    footStepsList.append([["RLeg"], [[0.00, -0.1, 0.0]]])

    # 4) Sidestep to the left with your left foot
    footStepsList.append([["LLeg"], [[0.00, 0.16, 0.0]]])

    # 5) Step backward & left with your right foot
    footStepsList.append([["RLeg"], [[-0.04, -0.1, 0.0]]])

    # 6)Step forward & right with your right foot
    footStepsList.append([["RLeg"], [[0.00, -0.16, 0.0]]])

    # 7) Move your left foot to your right foot
    footStepsList.append([["LLeg"], [[0.00, 0.1, 0.0]]])

    # 8) Sidestep to the right with your right foot
    footStepsList.append([["RLeg"], [[0.00, -0.16, 0.0]]])

    ###############################
    # Send Foot step
    ###############################
    stepFrequency = 0.8
    clearExisting = False
    nbStepDance = 2 # defined the number of cycle to make

    tts1.say("胡校长您好，欢迎来到山东大学创新创业大赛现场")

    t1=threading.Thread(target=test1,args=(nbStepDance,footStepsList,motionProxy1,motionProxy2,stepFrequency,clearExisting))
    t2=threading.Thread(target=test2,args=(nbStepDance,footStepsList,motionProxy1,motionProxy2,stepFrequency,clearExisting))
    t1.start()
    t2.start()
    global lock
    lock=True

    #motionProxy.post.waitUntilMoveIsFinished()



def test1(nbStepDance,footStepsList,motionProxy1,motionProxy2,stepFrequency,clearExisting):
    global lock
    while not lock:
        continue
    for j in range(nbStepDance):
        for i in range(len(footStepsList)):
            try:
                motionProxy1.post.setFootStepsWithSpeed(
                    footStepsList[i][0],
                    footStepsList[i][1],
                    [stepFrequency],
                    clearExisting)


            except Exception, errorMsg:
                print str(errorMsg)
                print "This example is not allowed on this robot."
                exit()
    motionProxy1.post.waitUntilMoveIsFinished()
    motionProxy2.waitUntilMoveIsFinished()

    # Go to rest position
    # motionProxy.post.rest()
    motionProxy1.post.rest()
    motionProxy2.rest()


def test2(nbStepDance,footStepsList,motionProxy1,motionProxy2,stepFrequency,clearExisting):
    global  lock
    while not lock:
        continue
    for j in range(nbStepDance):
        for i in range(len(footStepsList)):
            try:
                motionProxy2.post.setFootStepsWithSpeed(
                    footStepsList[i][0],
                    footStepsList[i][1],
                    [stepFrequency],
                    clearExisting)


            except Exception, errorMsg:
                print str(errorMsg)
                print "This example is not allowed on this robot."
                exit()
    motionProxy1.post.waitUntilMoveIsFinished()
    motionProxy2.waitUntilMoveIsFinished()

    # Go to rest position
    # motionProxy.post.rest()
    motionProxy1.post.rest()
    motionProxy2.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.106",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
