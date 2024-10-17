# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number
# that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical
# nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven
# otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome
# in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it
# to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a
# palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?

# put the expected answer here
expectedAnswer=249

import logging, math, timeit, time, psutil, platform, os


def isLychrel(n):

    for i in range(50):
        s = str(n)
        sr = s[::-1]
        ns = n + int(sr)
        if isPalindrome(ns):
            return False
        n=ns
    return True

def isPalindrome(n):
    s=str(n)
    if s==s[::-1]:
        return True
    return False

def solution():

    solution=0
    for i in range(10000):
        if isLychrel(i):
            solution+=1
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