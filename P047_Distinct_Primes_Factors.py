# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

# put the expected answer here
expectedAnswer=134043

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

def primeFactors(n):
    divisors = [ d for d in range(2,n//2+1) if n % d == 0 ]
    return [ d for d in divisors if all( d % od != 0 for od in divisors if od != d ) ]

def solution():
    # just a placeholder for where the solution to the problem will be stored and then returned
    solution=987654321

    #implement solution to the problem here
    consecutiveNumbersWithDistinctPrimes=0
    for i in range(1000000):
        if len(primeFactors(i))==4:
            consecutiveNumbersWithDistinctPrimes+=1
        else:
            consecutiveNumbersWithDistinctPrimes=0
        if consecutiveNumbersWithDistinctPrimes==4:
            solution=i
            break

    return solution-3 # because we stopped looping on the fourth number, and we want the first


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    stopwatch() #start timing
    solution = solution()
    timetaken=stopwatch() #stop timing
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))