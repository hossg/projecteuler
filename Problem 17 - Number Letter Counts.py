# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.


# could/should use the python package num2words, so this is in effect an alternative implementation

import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

onetonine=['one','two','three', 'four', 'five','six','seven','eight','nine']
onetonineteen=onetonine + ['ten','eleven','twelve','thirteen','fourteen','fifteen',
                           'sixteen','seventeen','eighteen','nineteen']
powersofTen=['ten','twenty','thirty','forty','fifty', 'sixty','seventy','eighty','ninety']

# A non-generic function that works for numbers upto and including 1000 only (as a special case)
# This could easily be generalised to work with triplets/larger numbers
def num2words(n):
    words=''
    if n==1000:
        words='one thousand'
        return words
    hundredsAndTens = divmod (n, 100)
    hundreds=hundredsAndTens[0]
    if hundreds >0:
        hundredsWords=onetonine[hundreds-1] + ' hundred'
        words += hundredsWords

    tens = hundredsAndTens[1]
    tensAndUnits = divmod(tens,10)
    if tens==0:
        return words
    elif hundreds>0:
        words += ' and '
    tensWords=''
    if tens<20:
        tensWords = onetonineteen[tens-1]
    else:
        tensWords = powersofTen[tensAndUnits[0]-1]
        unitsWords=''
        if tensAndUnits[1] > 0:
            unitsWords = onetonine[tensAndUnits[1]-1]
        tensWords += ' ' + unitsWords

    words +=  tensWords
    return words

#
# print(num2words(717))
# print(num2words(1000))
# print(num2words(727))
# print(num2words(707))
# print(num2words(13))
# print(num2words(1))
# print(num2words(20))
# print(num2words(30))
# print(num2words(37))

def solution():
    s=''
    #First build the string of words for the Problem
    for i in range (1001):
        s+=num2words(i)

    #Then strip out all of the spaces
    s = [c for c in s if c!=' ']
    sol=len(s)
    assert(sol==21124)

    logger.info('solution = {}'.format(sol))
    return sol

if __name__ == "__main__":
    solution()