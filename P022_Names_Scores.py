# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

import os
import logging
expectedAnswer = 871198282

logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

import csv


def score(s):
    score=0
    A=ord('A')-1    #ord returns the ordinal value of a character, i.e.the ASCII code by default
    for c in s:
        score += (ord(c) - A)
    return score

def solution():
    with open('p022_names.txt','r') as namesFile:
        names = csv.reader(namesFile)
        for row in names:
            sortedNames = sorted(row)
            logger.debug(sortedNames)

            totalscore=0
            for i,v in enumerate(sortedNames):
                s = score(v) * (i+1)        # enumerate will return zero-based index
                totalscore+=s

            logger.info('solution ={}'.format(totalscore))
            assert(totalscore==871198282)
            return totalscore

if __name__ == "__main__":
    solution()
