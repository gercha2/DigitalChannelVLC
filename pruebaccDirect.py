#import numpy as np
#import commpy.channelcoding.convcode as cc
#from commpy.utilities import dec2bitarray
import binascii
from pyb import DAC
import utime

#En esta prueba se crea un arreglo predefinido 
#con decimales del 0 al 255 y se envia cada 
#elemento del arreglo al DAC(1)
#***********************************************
# DAC parameters configuration
#***********************************************
dac = DAC(1, bits=8)
#***********************************************
#Conversion from text message into single decimal byte#
#***********************************************
msg = bytearray([255, 255, 0,  0, 255, 255, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0, 255, 255, 0, 0])
#msg = bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255])

#Ascci converted to hex and then to dec
for s in range(len(msg)):
	#msg_dec = int(binascii.hexlify(msg[s]), 16)
	dac.write(msg[s])

print(msg)
print(len(msg))
