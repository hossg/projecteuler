# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	Pn=n(3n−1)/2	    1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.

# put the expected answer here
expectedAnswer=1533776805

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

def Tn(n):
    return int(n*(n+1)/2)

def Pn(n):
    return int(n*(3*n - 1)/2)

def Hn(n):
    return int(n*(2*n-1))


def isTriangular(Tn):
    n=(math.sqrt(8*Tn+1)-1)/2
    if n==int(n):
        return True
    else:
        return False

def isPentangular(Pn):
    n=(math.sqrt(24*Pn+1)+1)/6
    if n==int(n):
        return True
    else:
        return False

def isHexangular(Hn):
    n = (math.sqrt((Hn + 1/8)/2) + 1/4)
    if n == int(n):
        return True
    else:
        return False


def solution():
    # just a placeholder for where the solution to the problem will be stored and then returned
    solution=None

    #implement solution to the problem here

    logging.debug('{} is triangular:{}'.format(Tn(285),isTriangular(Tn(285))))
    logging.debug('{} is pentangular:{}'.format(Pn(165),isPentangular(Pn(165))))
    logging.debug('{} is hexangular:{}'.format(Hn(143),isHexangular(Hn(143))))

    Hs=[]
    HsPs=[]
    logging.debug('Searching for Hexagonal numbers')
    for i in range(100000):
        H=Hn(i)
        Hs.append(H)
        if H>40755 and isPentangular(H) and isTriangular(H):
            return H

    return solution


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    stopwatch() #start timing
    solution = solution()
    timetaken=stopwatch() #stop timing
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))