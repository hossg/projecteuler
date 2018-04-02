# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
# form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
# number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
# English words, how many are triangle words?

import csv, math, logging

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getAlphaValue(x):
    return alphabet.index(x)+1

def wordValue(s):
    v=0
    for l in s:
        v+=getAlphaValue(l)
    return v

def triangleNumber(n):
    return n*(n+1)/2

def solution():
    with open('p042_words.txt','r') as wordsFile:
        reader = csv.reader(wordsFile)
        words = list(reader)[0]

        # work out the longest word needed, and thus the maximum word value, the largest triangle number needed
        longestWord=0
        for w in words:
            if len(w)>longestWord:
                longestWord=len(w)
        maximumWordValue=longestWord*26
        maximumN=int(math.sqrt(2*maximumWordValue))

        # calculate the needed triangle numbers
        triangleNumbers=[]
        for i in range(1,maximumN):
            triangleNumbers.append(triangleNumber(i))

        # and then simply tally how many words have values that are triangle numbers
        triangleWords=0
        for j in words:
            if wordValue(j) in triangleNumbers:
                triangleWords+=1

        return triangleWords

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution = solution()
    assert (solution == 162)
    logging.info('Solution = {}'.format(solution))
