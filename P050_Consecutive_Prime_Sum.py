# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# put the expected answer here
expectedAnswer=997651

import logging, math, timeit, time, psutil, platform, os

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

    # we will need both a list of primes, and a quick lookup to see whether a number IS prime
    isPrimes = sieve(1000001,onlyPrimes=False)
    primes = sieve(1000001,onlyPrimes=True)

    # for each prime number, build a sequence of the sums of it and all # subsequent primes, and store that sequence
    # in a dict keyed off the starting prime number
    primeSums={}
    for i,startingPrime in enumerate(primes):
        sequenceSums=[0]
        for prime in primes[i:]:        # start adding primes, for all the primes starting with the starting prime
            sum=sequenceSums[-1]+prime  # take the previous sum, and add the next prime
            if sum>=len(isPrimes)+2:    # we can stop as soon as we get to the limit of the range we're interested in
                break                   # +2 is just because the list of isPrimes *starts* with 2 in the zeroth slot
            sequenceSums.append(sequenceSums[-1]+prime) # otherwise, add the new running total to the sequence
        primeSums[startingPrime]=sequenceSums   # and when we're done, store the entire sequence in the dict, keyed off
                                                # the starting prime

    # now we're going to look at each sequence of sums we just generated, and for each one work backwards from the end
    # until we find the first prime number (from the end). This item will meet our broad criteria: it is a prime, and
    # it's the sum of a number of primes, starting with the starting prime for that sequence.
    maxP=1
    maxSequence=[]
    for p in primeSums:                                         # for each starting prime
        for i, e in reversed(list(enumerate(primeSums[p]))):    # 'e' will be the sum of primes, and i will be the index
                                                                # of that item from the start of the sequence, even
                                                                # though we are using 'reverse' to work from the back of
                                                                # the list.

            if e<len(isPrimes) and isPrimes[e-2]!=0:            # Allowing for +2 indexing, is this item prime?
                if i>maxP:                                      # If so, and if the index is further from the start than
                    maxP=i                                      # the greatest index found for other starting primes,
                                                                # then we have a new candidate solution.

                    maxSequence=primeSums[p][1:i+1]             # Since we're here, let's grab the actual sums for that
                                                                # solution

    solution = maxSequence[-1]                                  # The final sum of the longest sequence IS the prime
    i = primes.index(maxSequence[0])                            # Now let's also get the actual primes that combine
    primeSequence = [p for p in primes[i:i + len(maxSequence)]] # to give us that largest prime sequence total.

    logging.debug('Prime {} is the sum of {} primes starting at {}, has items: {}.'.format(solution, len(primeSequence),
                                                                                          maxSequence[0],primeSequence))

    return solution


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    stopwatch() #start timing
    solution = solution()
    timetaken=stopwatch() #stop timing
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))