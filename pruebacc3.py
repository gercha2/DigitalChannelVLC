#import numpy as np
#import commpy.channelcoding.convcode as cc
#from commpy.utilities import dec2bitarray
import binascii
from pyb import DAC
import utime


#***********************************************
#
#***********************************************
#msg = 'Hello World'
#msg = [0, 10, 30, 40, 50, 30, 0, 255, 0, 255, 0, 255, 0, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0, 255, 0]

info = range(0,255,1)
buf = bytearray(256)
for c in range(len(info)):
	buf[c] = info[c]

dac = DAC(1, bits=8)
dac.write_timed(buf, 100000 * len(buf), mode=DAC.CIRCULAR)

print(buf)
#print(msg_dec)
