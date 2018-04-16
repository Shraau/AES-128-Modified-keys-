import binascii
from binascii import hexlify
from collections import deque
def cyclicRotateright(input):
    return ([input[-1]] + input[0:-1])
def cyclicRotateleft(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]
def reverse(seq):
    SeqType = type(seq)
    emptySeq = SeqType()
     
    if seq == emptySeq:
        return emptySeq
     
    restrev = reverse(seq[1:])
    first = seq[0:1]
     
    # Combine the result
    result = restrev + first
     
    return result
 
#input is extra key of 8 characters 
text = input('Enter 8 characters string : ')
key = binascii.hexlify(text)
print ("Extra key:",key,"length of the extra key",len(key))
key_new = (bin(int(key,16)))[2:]
z = list(key_new)
length = len(z)
print ("length", length)
print(z)
print type(z)
print ('Rotatae to right',cyclicRotateright(z))
print ('Rotate to left',cyclicRotateleft(z,length))
print ('Reverse',reverse(z))
print (z.rotate(1))
