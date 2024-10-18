# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
# order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.


import itertools, logging

expectedAnswer = 16695334890

def generateTripletsDivisibleBy(n):
    triplets=[]
    for i in range(10,1000):
        s=str(i).zfill(3)
        if s[0] != s[1] and s[0] != s[2] and s[1] != s[2]:
            if(int(s)%n==0):
                triplets.append(s)
    return triplets

def generateAllBut(s):
    digits=list('0123456789')
    for d in s:
        digits.remove(d)
    allbut = []
    for d in itertools.permutations(digits):
        allbut.append(''.join(d))
    return allbut



def solution():

    # There are too many 10-digit pandigitals for us to scan them all, so we need to reduce the search space
    # significantly to begin with.  Our approach therefore is to build a candidate list of those where the last triplet
    # d8d9d10 is a multiple of 17, and then a subset of those where the prior triplet d7d8d9 is a multiple of 13.
    # The task then becomes trivial to filter out items which don't meet the other criteria.

    # First generate triplets that are divisible by 17.  All of our solutions will have to end with these digits
    t17=generateTripletsDivisibleBy(17)

    candidates=[]

    for n in t17:   # For each one of these, figure out every possible/valid 7-digit number that could preceed it
        allButN = generateAllBut(n)
        for m in allButN:  # And for each of *those* build the 3-digit d7d8d9 triplet that would be part of a valid solution
            s13=m[-1:]+n[0:2]
            if(int(s13)%13==0): # If that triplet is divisible by 13, then we have a candidate
                r=m+n
                candidates.append(r)

    # And now we have a managable list, incrementally filter down, triplet by triplet
    candidates = [x for x in candidates if int(x[5:8]) % 11 == 0]
    candidates = [x for x in candidates if int(x[4:7]) % 7 == 0]
    candidates = [x for x in candidates if int(x[3:6]) % 5 == 0]
    candidates = [x for x in candidates if int(x[2:5]) % 3 == 0]
    candidates = [x for x in candidates if int(x[1:4]) % 2 == 0]

    logging.debug(candidates)

    total=0
    for item in candidates:
        total+=int(item)

    return total


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution = solution()
    assert (solution == 16695334890)
    logging.info('Solution = {}'.format(solution))

