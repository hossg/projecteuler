import logging, os, time, subprocess


def get_primes(n):

    is_prime=get_sparse_primes(n)

    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

# Eratosthenes Sieve
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def get_sparse_primes(n):
    is_prime = [True] * n   # Assume all numbers are prime
    is_prime[0] = False     # But not 0 or 1
    is_prime[1] = False

    for p in range(n):
        if is_prime[p] is True:
            for i in range(2*p,n,p):
                is_prime[i]=False

    return is_prime


# Rather than use a home-built sieve method in Python, make use of primesieve library
# I did try to install pyprimesieve with a python/native interface but couldnt get it to install on my Mac
# Instead just do an ugly hack and call the tool via the command line and capture the output
def get_primes_fast(max_prime):
    logging.info("Generating primes")

    x = subprocess.run(['primesieve', '-p', str(max_prime)], stdout=subprocess.PIPE).stdout.decode('utf-8')
    y = x.split('\n')  # primesieve returns one prime per line
    z = y[:-1]  # and an irritating additional newline at the end
    primes = [int(n) for n in z]
    return primes

def get_prime_larger_than(n):
    sparse_primes=get_sparse_primes(n**2)
    n += 1
    while sparse_primes[n] == False:
        n += 1
    return n

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



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    stopwatch() #start timing
    logging.info('100 primes: {}'.format(get_primes(100)))
    p=get_primes(1000000)
    timetaken=stopwatch() #stop timing
    logging.info(timetaken)


    logging.info('100 primes: {}'.format(get_primes(100)))
    p = get_primes(1000000)
    timetaken=stopwatch() #stop timing
    logging.info(timetaken)

    logging.info('100 primes: {}'.format(get_primes_fast(100)))
    p = get_primes_fast(1000000)
    timetaken=stopwatch() #stop timing
    logging.info(timetaken)

    logging.info(get_prime_larger_than(17))