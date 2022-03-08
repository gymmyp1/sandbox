# a program to hopefully determine how large a chunk of indexes are the same
# in a sparse tensor.

import os, sys, getopt
import random
import math
import datetime
import numpy as np
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

            #nips/nell tensors
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

        highest_value = 0
        avg = 0
        for key, value in indexes.items():
            if value > highest_value:
                highest_value = value
            avg += value

        avg = avg/len(indexes)

        #retrieve highest 5 values
        top5avg = 0
        top5 = dict(Counter(indexes).most_common(5))
        print(top5)
        #for value in top5.items():
        #    top5avg += value

        #top5avg = avg/5

        print("overall average block density:",avg)
        print("top5avg: ",top5avg)
        print('highest block density:', highest_value)

        #should plot this...

if __name__ == "__main__":
   main()
