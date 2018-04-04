# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice
# a square.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

# put the expected answer here
expectedAnswer=5777

import logging, math, timeit, time, psutil, platform

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

def getsysteminfo():
    p=platform.platform()+' ' +platform.processor()+' Python: '+platform.python_version()
    memory=psutil.virtual_memory()
    cpuc=psutil.cpu_count()
    cpup=psutil.cpu_count(logical=True)
    cpuf=psutil.cpu_freq()
    cput=psutil.cpu_times_percent(percpu=False)

    return 'Platform: {}, Memory: {} Physical CPUs: {}, Logical CPUs: {}, Frequency (MHz): {}, Utilisation: {}'.format\
        (p,memory,cpuc,cpup,cpuf,cput)

# Eratosthenes Primes algorithm
def sieve(upperlimit):
    # mark off all multiples of 2 so we can use 2*p as the step for the inner loop
    l = [2] + [x if x % 2 != 0 else 0 for x in range(3, upperlimit + 1)]

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0

    # return l    # rather than return ONLY the primes, return primes and non-primes to allow super-fast, index-based
                # lookup of primes later on

    # filter out non primes from the list, not really that important i could work with a list full of zeros as well
    return [x for x in l if x]

def solution():
    # just a placeholder for where the solution to the problem will be stored and then returned
    solution=987654321

    #implement solution to the problem here

    # we're going to adopt a sieve style approach here, assuming that all composites can't be formed this way
    composites=[False]*10000 # arbitary but high range to search
    primes = sieve(10000)    # arbitary but high number of primes

    # and then filling in where they can be formed as per the conjecture
    for p in primes:
        for n in range(100):            # because this is the square root of the search space of 10000
            c=int(p+2*math.pow(n,2))
            if c<len(composites):
                composites[c]=True

    # and now scan through all of the odd numbers, looking for the first that hasn't been marked as True
    for index,value in enumerate(composites):
        if index%2 !=0 and  index>1 and value==False:
            return index



    return solution


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    stopwatch() #start timing
    solution = solution()
    timetaken=stopwatch() #stop timing
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))