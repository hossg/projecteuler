# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# spiral(1) = 1
# spiral(even) = undefined
# spiral(3) = starts at 3, then has numbers that are 3-1 apart i.e. 3,5,7,9, ends at 1  + 4*2 = 9
# spiral(5) = starts at 9 + (5-1), then has numbers (5-1) apart, and so ends at 9 + (4*4) = 9 + 16 = 25
# spiral(7) = starts at 25 + (7-1), then  has numbers (7-1) apart

expectedAnswer = 669171001

def spiral(l):
    if l==1:
        end=1
        sum=1

    else:
        end, sum = spiral(l-2)

        sumOfThisLevel = end + (l-1) + end + 2*(l-1) + end + 3*(l-1) + end + 4*(l-1)
        sum = sum + sumOfThisLevel
        end=end+4*(l-1)

    return (end, sum)

# for l in range(1,7,2):
#     print('{} - {}'.format(l,spiral(l)))

# print(spiral(1001))


assert spiral(1001)[1]==669171001

def solution():
    return spiral(1001)[1]
