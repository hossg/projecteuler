# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

# put the expected answer here
expectedAnswer=9110846700

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

def modularPow(n,p,mod):
    n = n % mod
    m=1
    for i in range(1,p+1):
        m=m*n
        m=m%mod
    return m

def solution():
    # just a placeholder for where the solution to the problem will be stored and then returned
    solution=987654321

    #implement solution to the problem here

    #the numbers involved are far too large for regular integers in Python, and the needed precision (least significant
    #10 digits are lost in floating point numbers, so we need another approach.  Modular arithmetic is the answer... as
    #we only need to keep the least significant 10 digits throughout the calculation

    t = 0
    for j in range(1,1001): # because we want the range to include the value 1000^1000
        t = t+modularPow(j,j,10000000000)
        t=t%10000000000

    solution = t

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