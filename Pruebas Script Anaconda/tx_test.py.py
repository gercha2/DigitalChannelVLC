#Sistema de Comunicaciones en una sola via, usando LI-FI;
#tx_msg = str('hello')
#SPB = 10
#transmisor
#tx_bs = []
#for carac in range(:len(tx_msg)):
#  character = tx_msg(carac)
#    byte = char2bin(character)
#
#program to generate a random bit sequence to be sent to VLC receiver
#Created by German Chavarro
#Oct 11 de 2016
#Declaration from library
import numpy as np
import binascii


tx_msg = "hello"
SPB = 10    #a sample bit rate is stablished

#generate a random bit sequence of 280 (Bytes)
message_bits = np.random.randint(0, 2, 2240)
b = bin(int(binascii.hexlify(tx_msg), 16))

#1-Otra manera de pasar de string to binary usando el modulo binascii
a = tx_msg.encode(encoding="utf-8", errors="ignore") #convert the string to hex

#2- Forma de pasar a binario un string
#tx_msg = "hello"
#SPB = 10
#tx_bs = 0;
#for c in range(len(tx_msg)):
#    byte = ord(tx_msg[c])        # find the 8-bit ASCII
#    a = np.binary_repr(byte)
#    tx_bs = [tx_bs + a]
#
# 
