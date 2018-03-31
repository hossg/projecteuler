# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.



import os
import logging
logger=logging.getLogger(os.path.basename(__file__))

def solution():
    max=0
    for i in range (1,1000):
        l=recurringCycle(i)
        logger.debug("{} - {}".format(i,l))
        if l > max:
            max = i
    logger.info("solution = {}".format(max))


def recurringCycle(d):
    for t in range (1,d):
        logger.debug("d={} t={} 10**t={} 10**t%d={}".format(d,t,10**t,10**t % d))
        if 1==10**t % d:
            return t
    return 0





if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution()