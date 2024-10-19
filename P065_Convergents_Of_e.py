# https://projecteuler.net/problem=65
from functools import lru_cache
import logging

expectedAnswer = 272

# 2,1,2,1,1,4,1,1,6,1,1,8,1,1,10,1,1,12,1,1,14,1,1,16,
def continued_fraction_of_e(k):
    if k == 0:
        return 2

    if (k - 5) % 3 == 0:
        return ((k + 1) // 3) * 2

    else:
        return 1


for k in range(12):
    logging.debug(continued_fraction_of_e(k))


def convergent(N, k):
    a0, ai = continued_fraction_sqrt(N)
    while k >= len(ai) - 1:
        ai = ai * 2
    print(k, ai)
    pk = convergent_p(a0, ai, k)
    qk = convergent_q(a0, ai, k)
    return pk, qk


@lru_cache(None)
def convergent_p(a0, ai, k):
    if k == 0: p = a0
    elif k == 1: p = a0 * ai[0] + 1
    else:
        p = ai[k - 1] * convergent_p(a0, tuple(ai), k - 1) + convergent_p(
            a0, tuple(ai), k - 2)
    return p


def convergent_q(a0, ai, k):
    if k == 0: q = 1
    elif k == 1: q = ai[0]
    else:
        q = ai[k - 1] * convergent_q(a0, ai, k - 1) + convergent_q(
            a0, ai, k - 2)
    return q


def solution():
    a0 = continued_fraction_of_e(0)
    ai = [continued_fraction_of_e(a) for a in range(1, 102)]
    logging.debug(a0, ai)
    convergent_numerators = [
        convergent_p(a0, tuple(ai), k) for k in range(0, 9)
    ]
    logging.debug(convergent_numerators)
    convergent_denominators = [convergent_q(a0, ai, k) for k in range(0, 9)]
    logging.debug(convergent_denominators)
    logging.debug(convergent_p(a0, tuple(ai), 9))
    logging.debug(digit_sum(convergent_p(a0, tuple(ai), 99)))
    return digit_sum(convergent_p(a0, tuple(ai), 99))


def digit_sum(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c)
    return sum

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



