#In this script, every ASCII character from text message is
#sent to DAC(1), so that can be created a digital waveform
#author: German Chavarro 23/02/2017

from ubinascii import hexlify, unhexlify
from pyb import DAC
#***********************************************
#parameters configuration
#***********************************************
SPB = int(10)

#***********************************************
#Conversion from text message into single decimal byte#
#***********************************************
msg = 'Hello World'
#SPB = 10
buf = bytearray('msg[c]')

for c in range(msg):
	buf(c) = unhexlify(msg[c], 'utf-8')

print(msg)
print(msgHex)
print(buf)




#for c in range(len(buf)):
	
#	data2 = array.array('B)

b#uf = bytearray(256*SPB)


	
#for c in range(len(msgHex)):
#	if msgHex == 1
#	buf[c] = msgHex[c]

#dac = DAC(1, bits=8)
#ac.write_timed(buf, 100000 * len(buf), mode=DAC.NORMAL)

#print(msg)
#print(msgHex)
#print(buf)

#from struct import *
#>>> pack('hhl', 1, 2, 3)
#b'\x00\x01\x00\x02\x00\x00\x00\x03'
#>>> unpack('hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03')
#(1, 2, 3)
#>>> calcsize('hhl'#)
