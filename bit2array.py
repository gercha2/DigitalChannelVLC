import numpy as np
 
__all__ = ['dec2bitarray', 'bitarray2dec', 'hamming_dist', 'euclid_dist', 'upsample']
 
def dec2bitarray(in_number, bit_width):
    """
    Converts a positive integer to NumPy array of the specified size containing
    bits (0 and 1).
 
    Parameters
    ----------
    in_number : int
        Positive integer to be converted to a bit array.
 
    bit_width : int
        Size of the output bit array.
 
    Returns
    -------
    bitarray : 1D ndarray of ints
        Array containing the binary representation of the input decimal.
 
    """
 
    binary_string = bin(in_number)
    length = len(binary_string)
    bitarray = np.zeros(bit_width, 'int')
    for i in range(length-2):
        bitarray[bit_width-i-1] = int(binary_string[length-i-1])
 
    return bitarray

a = dec2bitarray(255, 8)
print(a)
