#Produces inter-modal correlation matrices for tensors

import pandas as pd
import os, sys, getopt
sys.path.append('../')

df = pd.DataFrame(data,columns=['A','B','C'])
print(df)

# read the data in. It is assumed that the file contains information in the following format:
#   idx1 idx2 ... idxn value
# each index is stored as a tuple
indexes = []
with open(sys.argv[1], 'r') as file:
    for row in file:
        # read in the row and discard its value field
        row = row.split(' ')
        row.pop()

        # append the index
        indexes.append(tuple(int(i) for i in row))
