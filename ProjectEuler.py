# A runner that runs all of the Project Euler solutions
#
# This looks for all files in the current folder that begin Problem XX and then executes the problemXX() method therein

import timeit
import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

logger.info('Project Euler - Project Runner')
# get the list of files to play with and sort them numerically rather than alphabetically
import glob

files = glob.glob("Problem*.py")
def fileSort(name):
    return int(name.split()[1])

files=sorted(files, key = fileSort)

logger.info("Found {} problems to run".format(len(files)))
methodNames=[]
for k,i in enumerate(files):
    j=i.split()
    methodNames.append((j[0]+j[1]).lower())
    j=i.split(sep='.')
    files[k]=j[0]

# files=['Problem 25 - 1000-Digit Fibonacci number', 'Problem 1 - MultiplesOf3and5']
# methodNames=['problem25','problem1']
for k,i in enumerate(files):
    logger.info("Loading module: {}".format(i))
    f=__import__(i)
    result = f.solution()
    logger.info("Solution to {} = {}".format(i,result))

