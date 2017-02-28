from pyb import DAC
from binascii import hexlify, unhexlify
import utime
from struct import unpack

#create a text message
data = b'H'
for s in range(len(data)):
	h = hexlify(data[s])
	#hdec = unpack('<H', h)[0]
print(h)
#print(hdec)

#Parameters Fs=1MSPS
SPB=10

#Parameters for DAC
#dac = DAC(1, bits=12) #12 bits resolution
#dac.write(hdec)

#pyb.delay(100)
#print(hdec)
#print(type(hdec))
