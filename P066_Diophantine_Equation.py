# https://projecteuler.net/problem=66

# Consider quadratic Diophantine equations of the form:

# x^2–Dy^2=1

# For example, when D=13
# , the minimal solution in x
#  is 6492–13⋅1802=1
# .

# It can be assumed that there are no solutions in positive integers when D
#  is square.

# By finding minimal solutions in x
#  for D=2,3,5,6,7
# , we obtain the following:

# 32–2⋅22=1
# 22–3⋅12=1
# 92–5⋅42=1
# 52–6⋅22=1
# 82–7⋅32=1
# Hence, by considering minimal solutions in x
#  for D≤7
# , the largest x
#  is obtained when D=5
# .

# Find the value of D≤1000
#  in minimal solutions of x
#  for which the largest value of x
#  is obtained.

# Diophantine equation -> we're looking only at integer values of x and y, and also from
# the question, D is also an integer.
#
# So we can re-write the equation as y^2 = (x^2-1)/D and we know that this must be a
# perfect square

# Put the expected answer here
expectedAnswer = 661

import logging, os, math
from tqdm import tqdm
import P064_Odd_Period_Square_Roots

# import P065_Convergents_Of_e


# quick utility function to test if a number is a perfect square
def is_square(number):
    floor = int(math.sqrt(number))
    return floor**2 == number


# Naive solution - but this takes too long for some D
def naive_solution():
    max_x = 1
    max_D = 1
    D = 0
    for D in tqdm(range(1, 8), desc=f'D={D}'):
        if is_square(D):
            continue
        x = 2
        while True:
            x += 1
            if is_square((x**2 - 1) / D):
                if x > max_x:
                    max_x = x
                    max_D = D
                break

    return max_x, max_D


# Better solution
# Wikipedia shows this to be Pell's Equation: https://en.wikipedia.org/wiki/Pell%27s_equation
# And this page also shows a great way to find the 'fundamental' (minimal x) solutions, using
# continued fractions
#
def solution():
    max_x = 0
    max_d = 0
    for d in range(1, 1001):
        if is_square(d):
            continue
        x = get_minimal_x_solution(d)

        if x > max_x:
            max_x = x
            max_d = d

    return max_d


def evaluate_continued_fraction(a0, ai):
    # Initialize with the last element
    n, d = 1, 0  # since ai should not be empty if computation reaches here
    # Go backwards through ai to compute the full continued fraction
    for a in reversed(ai):
        n, d = d + n * a, n
    return a0 * n + d, n

def get_minimal_x_solution(d):
    a0, a = P064_Odd_Period_Square_Roots.continued_fraction_sqrt(d)
    logging.debug(f'a0 = {a0}, a = {a}')
    ll = len(a)
    ai = a[:-1] if ll % 2 == 0 else (a * 2)[:-1]
    x, y = evaluate_continued_fraction(a0, ai)

    logging.debug(
        f'd={d}: a0={a0}, ai={ai} x/y={x}/{y} {"EVEN" if ll % 2 == 0 else "ODD"}'
    )
    return x


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging = logging.getLogger(os.path.basename(__file__))
    logging.debug(evaluate_continued_fraction(2, [1, 1, 1]))
    s = solution()
    logging.debug('Solution = {}'.format(s))
    assert (s == expectedAnswer)
