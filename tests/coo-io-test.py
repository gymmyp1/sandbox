import os, sys, getopt
sys.path.append('../')

import sptensor.coo as coo

import time

def main(argv):
    printTensor = False
    for arg in argv:
        if arg == "-print":
            printTensor = True

    file = sys.argv[-1]
    #print('file: ', file)

    start_time = time.time()

    t = coo.read(file)
    if printTensor:
        coo.write(sys.stdout, t)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
   main(sys.argv[1:])
