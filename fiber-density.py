# a program to determine average and fiber density of a tensor.

import os, sys, getopt
import random
import math
import datetime
from scipy import stats
import numpy as np
import statistics
sys.path.append('../')

def main():
    #quick and dirty version for now

    # read the data in. It is assumed that the file contains information in the following format:
    #   idx1 idx2 ... idxn value
    # each index is stored as a tuple
    indexes = {}
    densities = {}
    sparsities = {}
    nell_2_rem_mode_dim = 28818 #removed mode dimension from nell-2
    nips_rem_mode_dim = 14036 #removed mode dimension from nips
    enron_rem_mode3_dim = 244268 #removed mode 3 dimension from enron
    enron_rem_mode4_dim = 1176 #removed mode 4 dimension from enron
    lbnl_rem_mode_dim = 868131 #removed mode 5 dimension from enron
    uber_rem_mode3_dim = 1140 #removed mode 3 dimension from uber
    uber_rem_mode4_dim = 1717 #removed mode 4 dimension from uber

    with open(sys.argv[1], 'r') as file:
        #determine what is the moving index
        # save the other 3 indexes

        for row in file:
            # read in the row and discard its value field
            row = row.split(' ')
            row.pop()
            #print(row)


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

            #now divide that number by the number of potential entries
            densities[curr_index] = indexes[curr_index]/nips_rem_mode_dim


        #statistics of the values in dictionary
        list_vals = list(densities.values())
        print("overall mean:",np.array(list_vals).mean())
        print("median:",statistics.median(list_vals))
        print("mode:", statistics.mode(list_vals))
        print("std deviation:",np.array(list_vals).std())
        print('highest fiber density:', max(list_vals))

        #should plot this...

if __name__ == "__main__":
   main()
