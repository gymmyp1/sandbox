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

print(morton.decode(827863656589,4))
print(morton.decode(860075911309,4))

#print(morton.encode(0,85,44))
#print(bin(morton.encode(0,85,44)))

#print(morton.encode([1,18,95]))
