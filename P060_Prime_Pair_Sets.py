# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
# result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
# 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import logging, math, timeit, time, platform, os, itertools, subprocess, random, psutil

# put the expected answer here
expectedAnswer = 26033


def concat(a, b):
    n = int(math.log10(b)) + 1
    a = a * (10 ** n)
    return a + b

# Miller–Rabin primality test
# One of the best algorithm to check if the given number if prime
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# Algorithm: http://bit.ly/2drtk0x
def is_prime(n, k=3):
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n % 2 == 0:  # should be faster than n % 2
        return False
    else:
        s, d = 0, n - 1
        while d % 2 == 0:
            s, d = s + 1, d >> 1
        # A for loop with a random sample of numbers
        for a in random.sample(range(2, n - 2), k):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    return False  # composite if we reached end of this loop
        return True  # probably prime if reached end of outer loop


def isprime_lookup(a, sieved_primes):
    if sieved_primes[a] == 0:
        return False
    else:
        return True


def get_prime_larger_than(n, sieved_primes):
    n += 1
    while sieved_primes[n] == 0:
        n += 1
    return n


def isprime_combinations(primes, sieved_primes):
    # logging.info(primes)
    for p in itertools.permutations(primes, 2):
        if not isprime_lookup(concat(p[0], p[1]), sieved_primes):
            return False
        if not isprime_lookup(concat(p[1], p[0]), sieved_primes):
            return False
    return True


def __get_primes(max_prime):
    logging.info("Generating primes")
    num_elements_in_set = 5
    max_prime_in_set = 9999
    max_prime = concat(max_prime_in_set, max_prime_in_set)
    # Rather than use a home-built sieve method in Python, make use of primesieve library
    # I did try to install pyprimesieve with a python/native interface but couldnt get it to install on my Mac
    # Instead just do an ugly hack and call the tool via the command line and capture the output
    x = subprocess.run(['primesieve', '-p', str(max_prime)], stdout=subprocess.PIPE).stdout.decode('utf-8')
    y = x.split('\n')  # primesieve returns one prime per line
    z = y[:-1]  # and an irritating additional newline at the end
    primes = [int(n) for n in z]
    return primes


def get_primes(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n ** 0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


def is_prime_pair(a, b):
    len_a = math.floor(math.log10(a)) + 1
    len_b = math.floor(math.log10(b)) + 1
    if is_prime(concat(a, b)) and is_prime(concat(b, a)):
        return True
    return False


def solution():
    potential_solutions = []
    primes = get_primes(9999)

    # a is first number
    for a in primes:
        # b is second number
        for b in primes:
            # check if b is less than a
            if b < a:
                continue
            # check if a and b satisfy the condition
            if is_prime_pair(a, b):
                # c is the third number
                for c in primes:
                    # check if c is less than b
                    if c < b:
                        continue
                    # check if a,c and b, c satisfy the condition
                    if is_prime_pair(a, c) and is_prime_pair(b, c):
                        # d is the fourth number
                        for d in primes:
                            # check if d is less than c
                            if d < c:
                                continue
                            # check if (a,d), (b,d) and (c,d) satisfy the condition
                            if is_prime_pair(a, d) and is_prime_pair(b, d) and is_prime_pair(c, d):
                                # e is the fifth prime
                                for e in primes:
                                    # check if e is less than d
                                    if e < d:
                                        continue
                                    # check if (a, e), (b, e), (c, e) and (d, e) satisfy condition
                                    if is_prime_pair(a, e) and is_prime_pair(b, e) and is_prime_pair(c,
                                                                                                     e) and is_prime_pair(
                                            d, e):
                                        logging.info('Potential solution: {} made up of {}'.format((a + b + c + d + e),
                                                                                                   (a, b, c, d, e)))
                                        potential_solutions.append(a + b + c + d + e)
    return min(potential_solutions)


# Utility function for measuring the performance of solutions
processtime = 0.0
walltime = 0.0


def stopwatch():
    global walltime, processtime
    wt = time.time()
    ct = time.clock()
    wtElapsed = wt - walltime
    ctElapsed = ct - processtime
    walltime = wt
    processtime = ct
    return ('Elapsed process time:{}s, Elapsed clock time:{}s'.format(ctElapsed, wtElapsed))


def getsysteminfo():
    p = platform.platform() + ' ' + platform.processor() + ' Python: ' + platform.python_version()
    memory = psutil.virtual_memory()
    cpuc = psutil.cpu_count()
    cpup = psutil.cpu_count(logical=True)
    cpuf = psutil.cpu_freq()
    cput = psutil.cpu_times_percent(percpu=False)

    return 'Platform: {}, Memory: {} Physical CPUs: {}, Logical CPUs: {}, Frequency (MHz): {}, Utilisation: {}'.format \
        (p, memory, cpuc, cpup, cpuf, cput)

    memory = psutil.virtual_memory()
    cpuc = psutil.cpu_count()
    cpup = psutil.cpu_count(logical=True)
    cpuf = psutil.cpu_freq()
    cput = psutil.cpu_times_percent(percpu=False)

    return 'Platform: {}, Memory: {} Physical CPUs: {}, Logical CPUs: {}, Frequency (MHz): {}, Utilisation: {}'.format \
        (p, memory, cpuc, cpup, cpuf, cput)
    return 'Platform: {}'.format(p)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging = logging.getLogger(os.path.basename(__file__))
    stopwatch()  # start timing
    solution = solution()
    timetaken = stopwatch()  # stop timing
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))
