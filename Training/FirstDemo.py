# -*- coding: utf-8 -*-
# Here's some new strange stuff, remember type it exactly.
#This is a demo for inputting arguments and functions.
from sys import argv

script, user_name = argv
prompt = '>'
print "Hi %s,I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)
print "Where do you live?"
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright,So you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes , lives , computer)

