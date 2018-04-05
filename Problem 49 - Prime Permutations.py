# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i)
# each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is
# one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

# put the expected answer here
expectedAnswer=296962999629

import logging, math, timeit, time, itertools, platform ,psutil

# TODO - re-enable the psutil package and behaviour (disabled because of install issues on Mac


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

    #First let's get all the 4-digit primes
    primes = sieve(9999)
    primes = [p for p in primes if p >= 1000]

    #let's now put all these primes into bags of those that share the same digits
    primebags={}
    for p in primes:
        digits = ''.join(sorted(str(p)))
        if digits in primebags:
                primebags[digits].append(p)
        else:
            primebags[digits]=[p]

    #now for each bag of primes that share the same digits, pull out every combination of 3 primes
    #and work out the difference between the first/second and second/third.  This works because
    #the primes are put into bags in increasing order, and that order is preserved by the
    #combinations method
    for k in primebags:
        primes = primebags[k]
        for p1,p2,p3 in itertools.combinations(primes, 3):
            if (p3-p2)==(p2-p1):
                logging.info('Found primes: {}, {}, {} which are {} apart.'.format(p1,p2,p3,p2-p1))
                if p1!=1487:
                    solution=str(p1)+str(p2)+str(p3)
                    break



    return int(solution)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    stopwatch() #start timing
    solution = solution()
    timetaken=stopwatch() #stop timing
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))

