# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Working out a simple upper limit to scan for: each digit in our number can contribute a maximum of 9^5 to the total
# this is 59049. 5 digits of this (i.e. 99999) could give us a maximum total of 295245, 6 digits would give us 354294
# 7 digits and above yield totals that are simply too short to add up to the number required.  Hence we should use the
# 6 digit total as our simple upper limit.

import timeit, logging

limit=354294


def solution():
    results=[]
    totalSum=0
    for n in range(2,limit):
        num=n
        s = 0
        while(num>0):
            d=num%10
            num = int(num/10)
            p=d*d*d*d*d #pow(d,5) - significantly faster, I presume because we don't need to implicitly cast to floating
                        # point numbers each time we call pow()
            s+=p
        if s==n:
            results.append(s)
            totalSum+=n
    assert totalSum==443839
    return totalSum


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging.info(solution())






