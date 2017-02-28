import numpy as np
import commpy.channelcoding.convcode as cc
from commpy.utilities import dec2bitarray
import binascii

#***********************************************
#Conversion from text message into binary array#
#***********************************************
msg = 'Hello World'
#Ascci converted to hex and then to dec
for s in range(len(msg)):
	msg_dec = int(binascii.hexlify(msg[s].encode(encoding='UTF-8' ,errors='strict')), 16)
num=8*len(msg)
#Convert decimal numbers into array
gen=dec2bitarray(msg_dec,num)
#***********************************************
# DAC parameters configuration
#***********************************************
SPB = 10
#for d in range(len(gen)):
#	data = gen(d)*SPB 
print(type(gen))
print(msg)
print(msg_dec)
print(num)
print(gen)
print(len(gen))
#print(data)

#++++++++++++++++++++++++++++++++++++++++++++++
# x = bytes('abc\x80def', 'utf-8') this part is recomended to convert string to byte
#+++++++++++++++++++++++++++++++++++++++++++++++
