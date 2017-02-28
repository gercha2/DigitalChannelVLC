#In this script is generated a bytearray and concatenated with ones and ceros
#Author: German Chavarro
#25/02/2017

import binascii
import numpy

tx_msg = bytes([1,1,1,0,0,1,1,1])
#tx_msg2 = b"Hello world"
#info = bin(int(binascii.unhexlify(tx_msg2), 16))
SPB = 30

tx_wave = bytes()
for i in range(len(tx_msg)):
    bit = tx_msg[i]
    if bit == 0:
        ceros = numpy.zeros((SPB,), dtype=numpy.byte)
        tx_wave = numpy.append(tx_wave, ceros, axis=None)
    else:
        unos = numpy.ones((SPB,), dtype=numpy.byte)
        tx_wave = numpy.append(tx_wave, unos, axis=None)

print(tx_wave)  