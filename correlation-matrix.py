# a script to print out correlation matrices between modes of a tensor.

import os, sys, getopt
import math
import pandas as pd
sys.path.append('../')

def main():
    # read the data in. It is assumed that the file contains information in the following format:
    #   idx1 idx2 ... idxn value
    # each index is stored as a tuple
    indexes = []
    with open(sys.argv[1], 'r') as file:
        for row in file:
            # read in the row and discard its value field
            row = row.split(' ')
            row.pop()

            # append the index as a list to the main list
            indexes.append(tuple(int(i) for i in row))

        #replace spaces with commas
        #import to pandas dataframe
        houses = pd.read_csv('data/melb_data.csv')
        houses.head()





if __name__ == "__main__":
   main()
