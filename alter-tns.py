# a program to alter an existing .tns file

import os, sys, getopt
import pandas as pd
sys.path.append('../')

#discard a mode
#mode - list of modes you want to discard
def drop_last_mode():
    # read the data in. It is assumed that the file contains information in the following format:
    #   idx1 idx2 ... idxn value
    # each index is stored as a tuple
    indexes = []
    with open(sys.argv[1], 'r') as file:
        for row in file:
            # read in the row and discard its value field
            row = row.split(' ')
            row.pop()
            row.pop() #also drop last mode

            # append the index as a list to the main list
            indexes.append(tuple(int(i) for i in row))

    #write updated indexes to new file
    with open(sys.argv[2], 'w') as file:
        for i in indexes:
            file.write(i + "\n")

def main():
    #need to make this function general but this is just cheap version
    drop_mode()




if __name__ == "__main__":
   main()
