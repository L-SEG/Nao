# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
# tts = ALProxy("ALTextToSpeech", "192.168.0.104", 9559)
# tts.setLanguage("Chinese")

tts1 = ALProxy("ALTextToSpeech", "192.168.1.106", 9559)
tts1.setLanguage("Chinese")

#motion = ALProxy("ALMotion","192.168.0.102",9559)
#motion .moveInit()
#id  = motion .post.moveTo(0.5,-0.5,0)
#motion.wait(id,0)
#tts.post.say("你好，我是NAO，我来自山东大学工程训练中心")
tts1.say("你好，我是NAO，我来自山东大学工程训练中心")

