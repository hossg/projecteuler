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
expectedAnswer=123456789

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
        replacementCombinations.append(substitutionString)
    return replacementCombinations

def autoreplacedigits(number, numberofreplacements):
    replacements=[]
    for i in range(10):
        replacements.append(replacedigits(number,str(i),numberofreplacements))
    return replacements

def autoautoreplacedigits(number):
    replacements=[]
    for i in range(1,len(str(number))+1):
        replacements.append(autoreplacedigits(number, i))


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

    primes=sieve(100000,onlyPrimes=True)
    isPrimes=sieve(100000,onlyPrimes=False)

    maxPrimeCount=0
    maxP=0
    iValue=0
    for p in primes:
        for i in range(1,len(str(p))+1):
            generatedNumbers=autoreplacedigits(p,i)

            for t in generatedNumbers:
                primeCount = 0
                for s in t:
                    # logging.info(s)
                    n=int(s)
                    if isPrimes[n-2] != 0:
                        primeCount+=1
                if primeCount==7: #>maxPrimeCount:
                    maxPrimeCount=primeCount
                    maxP=p
                    iValue=i
    logging.info('Smallest prime in family: {} Family count: {} i-value: {}'.format((maxP),maxPrimeCount,iValue))



    replacements = autoreplacedigits(123,2)
    for item in replacements:
        logging.debug(item)



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
    #assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))

