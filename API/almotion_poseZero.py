# -*- encoding:UTF-8 -*-
'''PoseZero:Set all the motors of the body to zero'''
import argparse
import time
from naoqi import ALProxy
def main(robotIP,PORT=9559):
    motionProxy = ALProxy("ALMotion",robotIP,PORT)
    postureProxy = ALProxy("ALRobotPosture",robotIP,PORT)
    #wake up the robot
    motionProxy.wakeUp()
    #send robot to stand zero
    postureProxy.goToPosture("StandZero",0.5)
    time.sleep(2)
    #we use the "body" name to signify the collection of all joints and actuactors
    #pName = "Body"
    #Get the Number of Joint
    #numBodies = len(motionProxy.getBodyNames(pNames))
    #we prepare a collection of floats
    #pMaxSpeedFraction = 0.3
    #ask motion to do this with a blocking call
    #motionProxy.angleInterpolationWithSpeed(pNames,pTargetAngles,pMaxSpeedFraction)
    #Go to rest position
    motionProxy.rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.106",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)