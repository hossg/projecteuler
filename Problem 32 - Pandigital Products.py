# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
# the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
# through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
# pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import logging, itertools, math


def isPandigitalTriplet(f1, f2, p):


    s1=str(f1)
    s2=str(f2)
    sp=str(p)
    s=s1+s2+sp
    o=sorted(s)


    if ''.join(o)=="123456789":
        return True
    else:
        return False


def getDigitsNotIn(n):
    s=sorted(set(str(n)))
    d = [x for x in range(1,10) if str(x) not in s]
    return d

def solution():

    results=[]

    # the product is necessarily larger than the factors
    # the largest factor we need to worry about is sqrt(987654321) since iterating beyond this will
    # start to duplicate factors already considered


    for a in range(int(math.sqrt(987654321))):

        sa=str(a)

        # if a contains a zero, then there's no way the triplet can be pandigital, so simply move on
        if '0' in sa:
            continue

        # if a has duplicate digits then there's no way the triplet can be pandigital, so simply move on
        if len(set(sa)) < len(sa):
            continue

        unuseddigits=getDigitsNotIn(a)

        # logging.debug('a={}'.format(a))
        # logging.debug('b has digits: {}'.format(unuseddigits))

        for lenb in range(len(unuseddigits)):  # for each length of unused digits
            for bdigits in itertools.permutations(unuseddigits,lenb): # figure out all permutations of numbers

                # logging.debug('bdigits: {}'.format(bdigits))
                # form a number from the digits
                b=0
                for d in bdigits:
                    b *= 10
                    b+=d

                f = a * b
                if isPandigitalTriplet(a, b, f):
                    logging.info("{} * {} = {}".format(a,b,f))
                    results.append(f)

    results = set(results)
    total=0
    for n in results:
        total+=n
    logging.info('Solution = {}'.format(total))
    assert (total==45228)
    return total


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution()