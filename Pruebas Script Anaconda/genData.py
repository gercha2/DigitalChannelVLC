# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:18:05 2016

@author: German
"""

import numpy
import binascii
#import commpy
tx_msg = b"Hello world"
#tx_msg = binascii.hexlify(b'Hello world')
tx_bs = bin(int(binascii.hexlify(tx_msg), 16))

SPB = 30

tx_wave = bytes()
for i in range(len(tx_msg)):
    bit = tx_msg[i]
    if bit == 0:
        ceros = numpy.zeros((SPB,), dtype=numpy.int)
        tx_wave = numpy.append(tx_wave, ceros, axis=None)
        dOut = tx_wave
    else:
        unos = numpy.ones((SPB,), dtype=numpy.int)
        tx_wave = numpy.append(tx_wave, unos, axis=None)
        dOut = tx_wave
print(dOut)  

#--------------------------------------------
#tx_msg2 = [0,1,0,1,0,1,0,1]
#tx_bs = bin(int(binascii.hexlify(b'tx_msg2'), 16))

#

tx_msg = [1, 1, 1, 0, 0, 1, 1, 1]
SPB = 30

tx_wave = bytes()
for i in range(len(tx_msg)):
    bit = tx_msg[i]
    if bit == 0:
        ceros = numpy.zeros((30,), dtype=numpy.byte)
        tx_wave = numpy.append(tx_wave, ceros)
        dOut = tx_wave
    else:
        unos = numpy.ones((30,), dtype=numpy.byte)
        tx_wave = numpy.append(tx_wave, unos)
        dOut = tx_wave

print(dOut)        
#---------------------------------------------------------
#CONCATENATE
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
#-------------------------------------------------------




