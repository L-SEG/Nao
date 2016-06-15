import serial
import time
t = serial.Serial('com5',9600)
n = t.write('sdfas\r\n')
print t.portstr
print n
time.sleep(1)
print str