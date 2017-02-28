#In this script, every ASCII character from text message is
#sent to DAC(1), so that can be created a digital waveform
#author: German Chavarro 23/02/2017

from ubinascii import hexlify
from pyb import DAC
#***********************************************
# DAC parameters configuration
#***********************************************


#***********************************************
#Conversion from text message into single decimal byte#
#***********************************************
msg = 'Hello World'
buf = bytearray(256)
msgHex = hexlify(msg)
	
for c in range(len(msgHex)):
	buf[c] = msgHex[c]

dac = DAC(1, bits=8)
dac.write_timed(buf, 100000 * len(buf), mode=DAC.NORMAL)

print(msg)
print(msgHex)
print(buf)
