# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

# put the expected answer here
expectedAnswer=127035954683

import logging, math, timeit, time, psutil, platform, os

import itertools


def prepareCubicNumbers(n):
    cubes = []
    for i in range (n):
        cubes.append(i**3)
    return cubes

def solution():
    # just a placeholder for where the solution to the problem will be stored and then returned
    solution=987654321
    cubes=[]
    n=0

    while True:
        cubeDigits = sorted(list(str(n**3)))    # for each possible cube, figure out the sorted set of digits
        cubes.append(cubeDigits)                # and record this
        c=cubes.count(cubeDigits)               # and see how many times we've had this set of digits... is it 5 yet?
        if c>=3:
            logging.debug('Cube with digits {} appears {} times so far'.format(cubeDigits,c))
        if c==5:
            solution=cubes.index(cubeDigits)**3 #  we want the index of the first number to
                                                #  produce this cube set, and hence the smallest
                                                #  cube, not the one that just triggered the
                                                #  threshold which would be the biggest of the 5!
            break
        n+=1

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