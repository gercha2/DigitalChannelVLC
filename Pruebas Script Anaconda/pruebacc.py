import numpy as np
import commpy.channelcoding.convcode as cc
from commpy.utilities import dec2bitarray
import binascii

#***********************************************
#Conversion from text message into binary array#
#***********************************************
msg = 'He'
#Ascci converted to hex and then to dec
msg_dec = int(binascii.hexlify(msg.encode(encoding='UTF-8' ,errors='strict')), 16)
num=8*len(msg)
#Convert decimal numbers into array
gen=dec2bitarray(msg_dec,num)
#***********************************************
SPB = 10
for d in range(len(gen)):
	data = gen(d)*SPB 
rint(type(gen))
print(msg)
print(msg_dec)
print(num)
print(gen)
print(len(gen))
print(data)


