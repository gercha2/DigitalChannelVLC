# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 18:20:12 2016

@author: German
"""

''' This progra try to implement a transmisor algorith in order to be send to
to the receiver
'''
tx_bs = []
tx_msg = 'hello'
for carac in range (len(tx_msg)):
    character = tx_msg(carac)       
    byte = char2dec(character)
    tx_bs = [tx_bs, byte]
