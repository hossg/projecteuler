# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a
# different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

# put the expected answer here
expectedAnswer=142857

import logging, math, timeit, time, psutil, platform, os

def digits(n):
    return ''.join(sorted(str(n)))

def solution():
    solution=0
    for i in range(1,1000000):
        d1 = digits(i)
        d2 = digits(2*i)
        d3 = digits(3*i)
        d4 = digits(4*i)
        d5 = digits(5*i)
        d6 =digits(6*i)
        if d1==d2 and d2==d3 and d3==d4 and d4==d5 and d5==d6:
            logging.info('{} {} {} {} {} {}'.format(i,2*i,3*i,4*i,5*i,6*i))
            solution=i


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
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    stopwatch() #start timing
    solution = solution()
    timetaken=stopwatch() #stop timing
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))