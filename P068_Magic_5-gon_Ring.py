# https://projecteuler.net/problem=68

# Ultimately we are looking for the biggest (concatenated/lexicographical) answers; for that reason we want to have the
# largest numbers on the outside, and the smaller numbers on the inside.
#
# So for a ring size of 3, with 6 digits, we want the numbers 1-3 on the inner ring, and the numbers 4-6 on the outer ring;
# for a ring size of 5, with 10 numbers, we want 1-5 on the inside and 6-10 on the outside.  Lexicographically, we also know
# that we want the two digit number 10 on the outside ring, so it doesn't get counted twice in the ring identification, pushing
# the result to 17 digits, rather than the 10 we are looking for.
#
# So we will generate permutations of the digits for the internal ring, and permutations of the digits for the external ring.
# For each of these we will test to see if it's a magic ring or not (totals are all the same) and if it is we will
# concatenate the ring definition, and see if it has a maximum value.


# Put the expected answer here
expectedAnswer=6531031914842725

import logging,os, itertools



def is_magic_ring(internal, external, ring_size):
    # Calculate the sum of each triplet and check if all sums are equal
    target_sum = external[0] + internal[0] + internal[1]
    for i in range(1, ring_size):
        if external[i] + internal[i] + internal[(i + 1) % ring_size] != target_sum:
            return False
    return True

def max_concatenation(internal, external, ring_size):
    # Find the line with the smallest external node to start the string
    start = external.index(min(external))
    result = []
    for i in range(ring_size):
        index = (start + i) % ring_size
        result.append(f"{external[index]}{internal[index]}{internal[(index + 1) % ring_size]}")
    return ''.join(result)

def solve5():
    max_solution = 0
    # External nodes are 6-10, internal nodes are 1-5
    for internal in itertools.permutations(range(1, 6)):
        for external in itertools.permutations(range(6, 11)):
            if is_magic_ring(internal, external,5):
                concat = max_concatenation(internal, external,5)
                if len(concat) == 16:
                    max_solution = max(max_solution, int(concat))
    return max_solution

def solve(ring_size):
    max_solution = 0
    # External nodes are 6-10, internal nodes are 1-5
    for internal in itertools.permutations(range(1, ring_size+1)):
        for external in itertools.permutations(range(ring_size+1, ring_size*2+1)):
            if is_magic_ring(internal, external,ring_size  ):
                concat = max_concatenation(internal, external,ring_size)
                # if len(concat) == 16:  # Ensuring it's a 16-digit solution, but perhaps redundant since 10 is definitely only counted once on the external ring
                max_solution = max(max_solution, int(concat))
    return max_solution


def solution():
    return solve(5)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    logging.debug(solve(3))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)
    