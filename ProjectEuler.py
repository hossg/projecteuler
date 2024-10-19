# A runner that runs all of the Project Euler solutions
#
# This looks for all files in the current folder that begin PXXX and then executes the solution() method therein

import timeit
import os
import logging
import re
import glob

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

logger.info('Project Euler - Project Runner')

# get the list of files to play with and sort them numerically rather than alphabetically
files = glob.glob("P0*.py")
logger.info("Found {} problems to run".format(len(files)))

modules = []
for k, i in enumerate(files):
    j = i.split(sep='.')
    modules.append(j[0])
modules = sorted(modules)

incorrectString = '\x1b[31;1mINCORRECT\x1b[0m'
correctString = '\x1b[32;1mCORRECT\x1b[0m'

# modules = ['P025_1000-Digit_Fibonacci_number', 'P001_MultiplesOf3and5']
for m in modules[65:]:
    logger.info(f"Loading module: {m}")
    f = __import__(m)
    expectedAnswer = f.expectedAnswer
    solution = f.solution()
    logger.info(
        f"Solution to {m} = {solution} {correctString if solution == expectedAnswer else incorrectString}"
    )
