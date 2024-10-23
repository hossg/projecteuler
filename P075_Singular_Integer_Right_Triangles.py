# It turns out that 12cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
# Put the expected answer here. In contrast, some lengths of wire, like 20cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120cm it is possible to form exactly three different integer sided right angle triangles.
# Given that L is the length of the wire, for how many values of L<1500000 can exactly one integer sided right angle triangle be formed?

# https://projecteuler.net/problem=75

# So - this is about pythagorean triples, so we presumably need to generate these up to a certain limit, and see what perimeters we can create, and make sure we then only include perimeters that are created once.

expectedAnswer = 161667

import logging, os, math
from collections import defaultdict


# Euclid's algorithm for generating primitive triples
def get_primitive_triple(m, n):
    a = m * m - n * n
    b = 2 * m * n
    c = m * m + n * n
    return (a, b, c)


# A little subsitution since we know P=a+b+c
# L = 2m^2+2mn
# n must be <m
def get_max_m(max_perimeter):
    return int(math.sqrt(max_perimeter / 2)) + 1


# This function calculates the answer and returns it
def solution():
    max_perimeter = 1500000
    perimeters = defaultdict(int)  # [0] * max_perimeter + [0]
    max_m = get_max_m(max_perimeter)

    for m in range(2, get_max_m(max_perimeter)):
        for n in range(1, m):

            if (m - n) % 2 == 1 and math.gcd(m, n) == 1: #m and n coprime and of opposite parities - see https://en.wikipedia.org/wiki/Pythagorean_triple#:~:text=Proof%20of%20Euclid's%20formula,-That%20satisfaction%20of&text=All%20such%20primitive%20triples%20can,to%20divide%20the%20third%20one).
            
                a,b,c = get_primitive_triple(m, n)
                perimeter = a + b + c

                # count the perimeter generated, as well as multiples of it                
                while perimeter <= max_perimeter:
                    perimeters[perimeter] += 1
                    perimeter += (a + b + c)

    total = 0
    for i in perimeters.values():
        if i == 1:
            total += 1

    singular_count = sum(1 for count in perimeters.values() if count == 1)
    return total


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging = logging.getLogger(os.path.basename(__file__))
    s = solution()
    logging.info('Solution = {}'.format(s))

    assert (s == expectedAnswer)
