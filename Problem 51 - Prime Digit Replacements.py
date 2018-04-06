# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
# 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having
# seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773,
# and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.

# put the expected answer here
expectedAnswer=121313

import logging, math, timeit, time, psutil, platform, os, itertools

def replacedigits(number, replacementdigit, numberofreplacements):
    s=str(number)
    numberofreplacements=min(numberofreplacements,len(s))
    replacementDigitCombinationSelector=[]
    for n in range(1,len(s)+1):
        replacementDigitCombinationSelector.append(n)
    replacementDigitCombinations=itertools.combinations(replacementDigitCombinationSelector,numberofreplacements)
    replacementCombinations=[]
    for r in replacementDigitCombinations:
        substitutionString=list(s)
        for d in r:
            substitutionString[d-1]=replacementdigit
        substitutionString=''.join(substitutionString)
        # logging.debug(substitutionString)
        replacementCombinations.append(int(substitutionString))
    return replacementCombinations

def autoreplacedigits(number, numberofreplacements):
    replacements=[]
    for i in range(10):
        replacements.append(replacedigits(number,str(i),numberofreplacements))
    return replacements




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
    isPrimes = sieve(1000000, onlyPrimes=False)
    primes=sieve(1000000,onlyPrimes=True)

    for p in primes:
        for i in range(1,len(str(p))+1):
            generatedNumbers=autoreplacedigits(p,i)
            generatedNumbers = list(map(list, zip(*generatedNumbers)))      # this just transposes our list of lists
                                                                            # our function varies the digits over a list
                                                                            # of varying positional substitutions; we
                                                                            # want it the other way around
            for t in generatedNumbers:
                primeCount = 0
                smallestPrime=t[-1] # start with the biggest and then replace with smaller primes
                for n in t:
                    if isPrimes[n-2] != 0 and len(str(n))==len(str(t[-1])):  # a hack - we only want to discount early
                                                                             # numbers where there may be leading zeros
                                                                             # dropped in the conversion to ints
                        primeCount+=1
                        smallestPrime=min(smallestPrime,n)
                if primeCount==8: #>maxPrimeCount:
                    logging.debug(t)
                    return smallestPrime



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

