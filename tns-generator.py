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
            temp = [0] * modes  #a list to hold randomly generated numbers

            temp = random.sample(range(dims[0]), k=len(moving_modes))
            for i in range(modes):
                if(i in moving_modes):
                    gen_index[i] = temp.pop()
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

    return indexes

#perturb index by an integer value and check if it's in range of indexes
def perturb_index(dims, key, fixed_index, mode_to_copy_to,perturb):
    gen_index = list(key)
    #shift the non-fixed index to the mode we want to copy to
    for i in gen_index:
        if i != fixed_index:
            perturbed_index = i+perturb

            #force index to be in valid range of our indices
            #check if this number if in range
            if perturbed_index < 0 and perturbed_index > dim[0]-1:
                #mod by dim[0]-1 to get it back in range
                print("perturbed index out of range:", perturbed_index)
                perturbed_index = perturbed_index % dim[0]-1
                print('new perturbed index:', perturbed_index)

            gen_index[mode_to_copy_to] = perturbed_index

    return gen_index

#Parameters:
# duplicate_mode: mode we want to copy over to other modes
# mode_to_copy_to: mode we want to duplicate a mode to
# perturn: integer to slightly shift an index up or down if we don't want to exactly duplicate
def duplicate_mode(dims, sparsity, moving_modes, fixed_index, duplicate_mode, mode_to_copy_to,perturb):
    indexes = fill_modes(dims, sparsity, moving_modes,fixed_index)

    new_indexes = {}

    with open(sys.argv[1], 'a') as file:
        for key in indexes:
            gen_index = perturb_index(dims, key, fixed_index, mode_to_copy_to, perturb)
            gen_index[duplicate_mode] = fixed_index #replace old mode value with fixed index
            gen_index = tuple(gen_index)  #convert back to tuple

            #check if perturbed index is already in our dictionary
            while gen_index in new_indexes:
                gen_index = list(gen_index) #convert to list and fix the perturbed index
                gen_index[mode_to_copy_to] += 1
                gen_index = tuple(temp_list) #convert back to tuple

            new_indexes[gen_index] = 1
            file.write(' '.join(map(str, gen_index)))
            file.write(" 1\n")

    #merge both dictionaries
    return(new_indexes.update(indexes))

def main():

    #gen_rand([10,10,10], 0.9)
    #fill_one_mode([100,100,100], 0.99, 1, 1)

    #Q. Does the hash favor flipping certain bits?
    #fill_modes([20000,20000,20000],0.99,[0],1)
    #fill_modes([20000,20000,20000],0.99,[1],1)
    #fill_modes([20000,20000,20000],0.99,[2],1)

    #Q. What happens if a mode is duplicated onto another mode?
    #duplicate_mode([20000,20000,20000],0.99, [0],1,0,1,0)
    duplicate_mode([500000,500000,500000],0.99, [0],1,0,1,0)

    #what happens if you perturb the copied mode slightly?
    #duplicate_mode([20000,20000,20000],0.99, [0],1,0,1,100)
    #duplicate_mode([50000,50000,50000],0.99, [0],1,0,1,100)


    print("Sparse tensor generated.")

if __name__ == "__main__":
   main()
