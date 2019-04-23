# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
# result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
# 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# put the expected answer here
expectedAnswer=123456789

import logging, math, timeit, time,  platform, os, itertools, subprocess
# import psutil


def concat(a,b):
    n=int(math.log10(b))+1
    a=a*(10**n)
    return a + b

def strconcat(a,b):
    return int(str(a)+str(b))

def set_of_primes(c):


def solution():

    logging.info("Generating primes")
    num_elements_in_set=5
    max_prime_in_set=999
    max_prime=concat(max_prime_in_set,max_prime_in_set)
    # Rather than use a home-built sieve method in Python, make use of primesieve library
    # I did try to install pyprimesieve with a python/native interface but couldnt get it to install on my Mac
    # Instead just do an ugly hack and call the tool via the command line and capture the output
    x = subprocess.run(['primesieve', '-p', str(max_prime)], stdout=subprocess.PIPE).stdout.decode('utf-8')
    y = x.split('\n')   # primesieve returns one prime per line
    z = y[:-1]          # and an irritating additional newline at the end
    primes = [int(n) for n in z]

    logging.info("Generating sparse primes")
    # now generate a sparse array to contain the primes - this massively optimises prime-lookup speed compared with
    # simply doing  if x in y list lookup
    max_prime = primes[-1]
    sparse_primes=[0]*(max_prime+1)
    for i in primes:
        sparse_primes[i]=i

    logging.info("Preparing search sets")
    primes_to_use=[p for p in primes if p<=max_prime_in_set]
    search_sets=set(itertools.combinations(primes_to_use, num_elements_in_set))
    search_sets = (itertools.combinations(primes_to_use, num_elements_in_set))

    logging.info("Searching for prime pairs with minimal sum")
    lowest_sum=99999999999

    # for c in [ (3,7,109,673,n) for n in primes[:int(len(primes)/1000)]]:
    for c in search_sets:
        #logging.info("Testing {}".format(c))
        all_combinations_prime=True
        for s in itertools.combinations(c,2):
            # n0 = str(s[0])
            # n1 = str(s[1])
            # s0 = n0+n1
            # s1 = n1+n0
            m0 = concat(s[0],s[1])
            m1 = concat(s[1],s[0])
            if sparse_primes[m0] ==0 or sparse_primes[m1]==0:
                all_combinations_prime=False
                break
        if all_combinations_prime:
            total=sum(c)
            logging.info("Valid prime combination: {}, total: {}".format(c,total))
            if total < lowest_sum:
                lowest_sum=total

    logging.info('Lowest sum: {}'.format(lowest_sum))

    #implement solution to the problem here
    time.sleep(1)

    return lowest_sum


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
    # memory=psutil.virtual_memory()
    # cpuc=psutil.cpu_count()
    # cpup=psutil.cpu_count(logical=True)
    # cpuf=psutil.cpu_freq()
    # cput=psutil.cpu_times_percent(percpu=False)

    # return 'Platform: {}, Memory: {} Physical CPUs: {}, Logical CPUs: {}, Frequency (MHz): {}, Utilisation: {}'.format\
    #     (p,memory,cpuc,cpup,cpuf,cput)
    return'Platform: {}'.format(p)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    stopwatch() #start timing
    solution = solution()
    timetaken=stopwatch() #stop timing
    #assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))

stopwatch() #start timing
print(concat(1234,70))
print(concat(70,1234))
for n in range(10000):
    x=concat(12345,76543)
timetaken=stopwatch() #stop timing
print(timetaken)

stopwatch() #start timing
print(strconcat(1234,70))
print(strconcat(70,1234))
for n in range(10000):
    x=strconcat(12345,76543)
timetaken=stopwatch() #stop timing
print(timetaken)