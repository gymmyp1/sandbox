#a file to quickly encode/decode values for example purposes.

import os, sys, getopt
import math
sys.path.append('../')

import sptensor.morton as morton

'''Parameters:
    m - The morton encoded set
    n - The number of integers present
Returns:
    The list of decoded integers'''

morton = morton.encode(1,8,16,1)
print(morton)
print(bin(morton))
print("key = ",int(101001000101010110101100101101101)%8388608)

#print(morton.decode(morton,4))
