# -*- encoding:UTF-8 -*-
""" Say "hello,Human" each time a human face is detected
"""
import sys
import time
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "192.168.0.104"

# GLobal variable to store the HumanGreeter module instance
HumanGreeter  = None
memory = None

class HumanGreeterModule(ALModule):
    """A simple module able to react to
    facedetection events"""

    def __init__(self,name):
        ALModule.__init__(self,name)
        #No need for IP and port here
        #because we have our Python broker connected to NAOqi broker

        #Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")
        #Suscribe to the FaceDetected event:
        global memory
        memory  = ALProxy("ALMemory")
        memory.subscribeToEvent("FaceDetected","HumanGreeter","onFaceDetected")

    def onFaceDetected(self,*_args):
        """This will be called each time a face is detected.
        """
        #Unsubscribe to the event whern talking,
        #to avoid repetitions
        memory.unsubscribeToEvent("FaceDetected","HumanGreeter")

        self.tts.say("Hello,Human")
        #Subscribe again to the event
        memory.subscribeToEvent("FaceDetected","HumanGreeter","onFaceDetecred")

def main():
    """main entry point
    """
    parser =  OptionParser()
    parser.add_option("--pip",
                      help = "Parent broker port.The IP address or your robot",
                      dest = "pip")
    parser.add.option("--pport",
                      help = "parent broker port. The port NAOqi is listening to",
                      dest="pport",
                      type = "int")
    parser.set_defaults(pip=NAO_IP,
                        pport=9559)

    (opts,args_) = parser.parse_args()
    pip = opts.pip
    pport = opts.pport

    #We need this broker to be able to construct NAOqi modules and subscribe to other modules
    #The broker must stay alive until the program exists
    myBroker  =  ALBroker("myBroker","0.0.0.0",
                          0,
                          pip,
                          pport)
                      
    #Warning:HumanGreeter must be a global variable
    #The name given to the constructor must be the name of the variable
    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)

    if __name__ == "__main__":
       main()
       
