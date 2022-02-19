# Simulated tensor generator.
# Makes an entry for every index.

import os, sys, getopt
import random
import math
import datetime
import numpy as np
sys.path.append('../')

#requires symmetrical dimensions
def gen_rand(dims, sparsity):
    #create empty dictionary, composed of indexes
    indexes = {}
    gen_index = [] #current generated index
    modes = len(dims)
    total = 1

    for i in range(modes):
        total *= dims[i]

    #calculate number of nonzero entries
    nnz = math.ceil(total-(total*sparsity))

    with open(sys.argv[1], 'w') as file:
        #generate nnz's worth of triplets/quadruples/etc
        while(len(indexes) < nnz):
                    #generate index into a tuple
                    gen_index = tuple(random.sample(range(dims[0]), k=modes))

                    if gen_index not in indexes:    #make sure there's no duplicates
                        indexes[gen_index] = 1 #add entry to dictionary
                        file.write(' '.join(map(str, gen_index)))
                        file.write(" 1\n")


#fix all but one mode, fill remaining mode with entries according to desired sparsity
#fixed index is what index do we want to keep same
#moving mode - what mode we want to vary
def fill_one_mode(dims, sparsity, moving_mode, fixed_index):
    #create empty dictionary, composed of indexes
    indexes = {}
    gen_index = [] #current generated index
    modes = len(dims)
    total = 1

    for i in range(modes):
        total *= dims[i]

    #calculate number of nonzero entries
    nnz = math.ceil(total-(total*sparsity))
    print('nnz:', nnz)


    with open(sys.argv[1], 'w') as file:
        #generate nnz's worth of triplets/quadruples/etc
        while(len(indexes) < nnz):
            gen_index = [0] * modes
            #generate the one random number
            #print("generating rand number")
            temp = random.randint(0, dims[0])
            for i in range(modes):
                if(i == moving_mode):
                    gen_index[i] = temp
                else:
                    gen_index[i] = fixed_index

            #convert to a tuple
            gen_index = tuple(gen_index)

            #check if it exists yet
            if gen_index not in indexes:
                indexes[gen_index] = 1
                file.write(' '.join(map(str, gen_index)))
                file.write("1\n")
                print("added one entry- ", len(indexes))
                print(gen_index)

        #copy what we did to another mode


# Fill and fix an arbitrary number of modes
# Parameters:
# moving_modes - a list of what modes that you are not fixing
# fixed_index - what index fixed modes should equal
def fill_modes(dims, sparsity, moving_modes, fixed_index):
    #create empty dictionary, composed of indexes
    indexes = {}
    gen_index = [] #current generated index
    modes = len(dims)
    total = 1

    for i in range(modes):
        total *= dims[i]

    #calculate number of nonzero entries
    nnz = math.ceil(total-(total*sparsity))
    print(nnz)

    #total possible indexes, in case nnz is greater than that (in that case it never stops T_T)
    total = 1
    for i in range(len(moving_modes)):
        total *= dims[moving_modes[i]]
    poss_indexes = total
    print("total possible indexes:",total)

    with open(sys.argv[1], 'w') as file:
        while(len(indexes) < nnz):
            gen_index = [0] * modes

            temp = random.sample(range(dims[0]), k=len(moving_modes))
            for i in range(modes):
                if(i in moving_modes):
                    gen_index[i] = temp[i]
                else:
                    gen_index[i] = fixed_index

            #convert to a tuple
            gen_index = tuple(gen_index)

            #check if it exists yet
            if gen_index not in indexes:
                indexes[gen_index] = 1
                file.write(' '.join(map(str, gen_index)))
                file.write(" 1\n")

                if len(indexes) % 1000 == 0:
                    print("Total number of entries- ", len(indexes))
                    print(gen_index)

                #if we've reached the limit of possible indexes, break out of loop
                if len(indexes) == poss_indexes:
                    print('number of possible indexes reached.')
                    break

def main():

    #gen_rand([10,10,10], 0.9)
    #fill_one_mode([100,100,100], 0.99, 1, 1)
    fill_modes([20000,20000,20000],0.99,[0],1)

    print("Sparse tensor generated.")

if __name__ == "__main__":
   main()
