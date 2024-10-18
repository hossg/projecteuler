

# put the expected answer here
expectedAnswer=4075

import logging, math, timeit, time, psutil, platform, os


def C(n,r):
    c = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    return c





def solution():

    largeCombinations = 0
    for n in range(101):
        for r in range(n + 1):
            if C(n, r) > 1000000:
                largeCombinations += 1
                logging.debug('Found C({},{}) = {}'.format(n, r, C(n, r)))

    solution=largeCombinations

    return solution


# Utility function for measuring the performance of solutions
processtime=0.0
walltime=0.0
def stopwatch():
    global walltime, processtime
    wt=time.time()
    ct=time.clock()
    wtElapsed=wt-walltime
    ctElapsed=ct-processtime
    walltime=wt
    processtime=ct
    return('Elapsed process time:{}s, Elapsed clock time:{}s'.format(ctElapsed,wtElapsed))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
#    logging=logging.getLogger(os.path.basename(__file__))
    stopwatch() #start timing
    solution = solution()
    timetaken=stopwatch() #stop timing
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
#    logging.info('System info: {}'.format(getsysteminfo()))
