# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# put the expected answer here
expectedAnswer=123456789

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
def sieve(upperlimit, onlyPrimes=False):
    # mark off all multiples of 2 so we can use 2*p as the step for the inner loop
    l = [2] + [x if x % 2 != 0 else 0 for x in range(3, upperlimit + 1)]

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0

    if onlyPrimes==False:
        return l    # rather than return ONLY the primes, return primes and non-primes to allow super-fast, index-based
                # lookup of primes later on

    # filter out non primes from the list, not really that important i could work with a list full of zeros as well
    else:
        return [x for x in l if x]


def solution():
    # just a placeholder for where the solution to the problem will be stored and then returned
    solution=987654321

    isPrimes = sieve(1001)
    primes = sieve(1001,onlyPrimes=True)

    longestSequenceStartingPrime=0
    totalOfLongestSequence=0
    for i,p in enumerate(primes):
        total=p
        previoustotal=p
        currentSequenceLength=1
        for nextp in primes[i+1:]:
            total+=nextp

            if total <1000 and isPrimes[total-2]!=0:
                currentSequenceLength+=1
                previoustotal=total
            else:
                break
        if currentSequenceLength>longestSequenceStartingPrime:
            longestSequenceStartingPrime=p
            totalOfLongestSequence=previoustotal
    logging.info('Sequence starts with {} and totals to {}'.format(longestSequenceStartingPrime,totalOfLongestSequence))



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