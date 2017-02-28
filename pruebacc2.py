#import numpy as np
#import commpy.channelcoding.convcode as cc
#from commpy.utilities import dec2bitarray
import binascii
from pyb import DAC
import utime


#***********************************************
# DAC parameters configuration
#***********************************************
dac = DAC(1, bits=8)

#***********************************************
#Conversion from text message into single decimal byte#
#***********************************************
msg = 'Hello World'
#Ascci converted to hex and then to dec
for s in range(len(msg)):
	msg_dec = int(binascii.hexlify(msg[s]), 16)
	dac.write(msg_dec)
	#pyb.delay(50)

print(msg)
print(msg_dec)
