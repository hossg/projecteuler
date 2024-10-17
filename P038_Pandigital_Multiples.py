# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
#  of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
# (1,2, ... , n) where n > 1?

import logging

def concatenatedProduct(n,m):
    s =''
    for i in range(1,m+1):
        s += str(n*i)
    return s

def is9DigitPandigital(s):
    st=sorted(s)
    if ''.join(st) == "123456789":
        return True
    else:
        return False


def solution():
    currentHighestSolution=0

# if n > 1, then we will have at least two products to concatenate, the second double the size of the former.
# So the second must be 5 digits long (at most) and the first 4 digits long at most.
# The maximum value of a 4-digit contributor to a 9-digit pandigital is 9876, and so this should the highest value
# of our outer loop
    maxN=9876
    maxM=9  # the inner loop maxes out at 9 since the concatenation cannot be more than 9 characters and be valid

    for n in range(maxN):
        for m in range(maxM):
            x=concatenatedProduct(n,m)
            if is9DigitPandigital(x):
                i=int(x)
                logging.info('({},{}) -> {}'.format(n, m, x))
                if i>currentHighestSolution:
                    currentHighestSolution=i
    return currentHighestSolution

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution=solution()
    assert (solution==932718654)
    logging.info('Solution = {}'.format(solution))


