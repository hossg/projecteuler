# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing
# two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# so denominator and numerator run from 10 to 99 (two digits) but we can also exclude 10 as a denominator, as otherwise we would leave a
# a zero denominator (since cancelling zeros is considered a trivial solution).


import math, logging

def digits(n):
    n2 = n % 10
    n1 = int((n - n2)/10)
    return (n1,n2)

def complete_solution():
    results = []
    for d in range(11,99+1):
        d1,d2=digits(d)

        for n in range(10,d+1):
            n1,n2=digits(n)

            if n2==0:
                continue

            f=0
            if n1==d1 and d2!=0:
                f=n2/d2
            elif n1==d2 and d1!=0:
                f=n2/d1
            elif n2==d1 and d2!=0:
                f=n1/d2
            elif n2==d2 and d1!=0:
                f=n1/d1

            if f < 1 and f == n/d:
                results.append((n,d))
    logging.debug('Valid digit-cancelling fractions, (numerator, denominator): {}'.format(', '.join(map(str,results))))
    return results


def solution():
    num = den = 1
    for i in complete_solution():
        num = num * i[0]
        den = den * i[1]

    gcd = math.gcd(num, den)
    logging.debug('Numerator: {}'.format(num))
    logging.debug('Denominator: {}'.format(den))

    soln = den/gcd
    assert(soln==100)

    return soln


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging.info('solution={}'.format(solution()))











