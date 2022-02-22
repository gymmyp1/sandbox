# a script to perturb a real world sparse tensor data set.

# Usage: file.py [file-output] [modes to fill]
#[modes to fill] are a comma delimited list of modes with no spaces.

import os, sys, getopt
import math
import pandas as pd
sys.path.append('../')

def main():
    #get the list of modes you want to fill
    fill_modes = sys.argv[2]
    fill_modes = fill_modes.split(",") #convert to list of numbers
    print(fill_modes)

    # read the data in. It is assumed that the file contains information in the following format:
    #   idx1 idx2 ... idxn value
    # each index is stored as a tuple
    indexes = {}
    curr_index = []

    with open(sys.argv[1], 'r') as file:
        for row in file:
            # read in the row and discard its value field
            row = row.split(' ')
            row.pop()

            for i in row:
                if i in fill_modes:
                    #add that index to dictionary of indexes we need to fill
                    indexes.append(tuple(int(i) for i in row))


        #replace spaces with commas
        #import to pandas dataframe
        houses = pd.read_csv('data/melb_data.csv')
        houses.head()
