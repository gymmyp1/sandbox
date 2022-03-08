# a program to hopefully determine how large a chunk of indexes are the same
# in a sparse tensor.

import os, sys, getopt
import random
import math
import datetime
from scipy import stats
import numpy as np
import statistics
from collections import Counter
sys.path.append('../')

def main():
    #quick and dirty version for now

    # read the data in. It is assumed that the file contains information in the following format:
    #   idx1 idx2 ... idxn value
    # each index is stored as a tuple
    indexes = {}
    #moving_indexes = map(int,sys.argv[2].split(',') )

    with open(sys.argv[1], 'r') as file:
        #determine what is the moving index
        # save the other 3 indexes

        for row in file:
            # read in the row and discard its value field
            row = row.split(' ')
            row.pop()
            #print(row)

            #remove moving indexes
            '''for i in moving_indexes:
                print(row[i])
                row.pop(i)'''

            #nips/nell-2 tensors
            row.pop(2)

            #enron
            #row.pop(2)
            #row.pop(3)

            #uber
            #row.pop()
            #row.pop()

            #lbnl
            #row.pop(4)

            # append the index as a list to the main list
            curr_index = tuple(int(i) for i in row)

            #check if the first 4 indexes are the same
            if curr_index not in indexes:
                # if not, add the new index to our dictionary & set it to be the new one to compare to
                indexes[curr_index] = 1
                #print("new index found:", curr_index)
            else:
                indexes[curr_index] += 1
                #print('repeat of index: ', curr_index)

        #statistics of the values in dictionary
        list_vals = list(indexes.values())
        print("overall mean:",np.array(list_vals).mean())
        print("median:",statistics.median(list_vals))
        print("mode:", statistics.mode(list_vals))
        print("std deviation:",np.array(list_vals).std())
        print('highest block density:', max(list_vals))

        #should plot this...

if __name__ == "__main__":
   main()
