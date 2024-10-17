# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions
# for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

# So - finding primitive pythagorean triples, using Euclid's formula:
# a=m^{2}-n^{2}, b=2mn, c=m^{2}+n^{2}
# and then multiplying by a factor K to find non-primitive solutions

import logging, math


# Generate enough triples (as long as we create one side of the triangle to be up to 1000, we know we won't need to go
# higher
def solution():
    solutions=[]
    for i in range(1,1001):
        solutions.append([])
    for a in range(1,1000):
        for b in range(1,a):
            c=math.sqrt(math.pow(a,2)+math.pow(b,2))
            if c%1==0:
                c=int(c)

                p=a+b+c
                if p<1000:
                    logging.info('Found a valid triple: {} = {}+{}+{}'.format(p,a, b, c))
                    solutions[p].append((p,a,b,c))

    # Now scan through the solutions for every perimeter we've found, to find the one with the most solutions
    maxlength=0
    itemmax=[]
    for item in solutions:
        if len(item)>maxlength:
            itemmax=item
            maxlength=len(item)
    logging.info('P={} has {} solutions: {}'.format(itemmax[0][0],len(itemmax),itemmax))
    return (itemmax[0][0])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution=solution()
    assert (solution==840)
    logging.info('Solution = {}'.format(solution))