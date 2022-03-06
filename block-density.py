# a program to hopefully determine how large a chunk of indexes are the same
# in a sparse tensor.

import os, sys, getopt
import random
import math
import datetime
import numpy as np
sys.path.append('../')

'''def read_file():
    # read the data in. It is assumed that the file contains information in the following format:
    #   idx1 idx2 ... idxn value
    # each index is stored as a tuple
    indexes = []
    with open(sys.argv[1], 'r') as file:
        #determine what is the moving index
        # save the other 3 indexes



        for row in file:
            # read in the row and discard its value field
            row = row.split(' ')
            row.pop()

            # append the index as a list to the main list
            indexes.append(tuple(int(i) for i in row))
            '''

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

            #nips tensor
            #row.pop(2)

            #uber
            #row.pop()
            #row.pop()

            #lbnl

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

        #print(indexes)
        highest_value = 0
        for key, value in indexes.items():
            if value > highest_value:
                highest_value = value
                #print(key,value)

        print('highest block density:', highest_value)

if __name__ == "__main__":
   main()
