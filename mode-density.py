# a program to calculate the density of a mode.
import os, sys, getopt
import pandas as pd
sys.path.append('../')

def main():
    dims = [2482, 2862, 14036, 17]
    modes = len(dims)

    total = 1
    for i in range(modes):
        total*=dims[i]

    nnz = 3101609
    nz = total - nnz    #total number of zeroes in tensor

    ratio = nz/total
    print("ratio of 0s:", ratio)

    for i in range(modes):
        sparsity = 1-(ratio/dims[i])
        print("sparsity along mode " + str(i) + ": " + str(sparsity))


if __name__ == "__main__":
   main()
