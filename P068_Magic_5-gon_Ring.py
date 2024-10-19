# Put the problem description here, including a link to the problem on the website if available.

# Put the expected answer here
expectedAnswer=123456789

import logging,os, itertools


def ring3():
    numbers=list(range(1,7))*2 # because each number can be used at most twice, if in the inner ring
    permutation_length=9
    possibilities = (itertools.permutations(numbers,permutation_length))
    maxRingVal=0
    for i in possibilities:
        if isValid3Ring(i):
            ringVal = concatRing(i)
            logging.debug(f'{sum(i[0:3])}: {ringVal}')
            if ringVal > maxRingVal:
                maxRingVal = ringVal
    logging.debug(f'Max Ring Value: {maxRingVal}')  
    return maxRingVal

def ring5():
    numbers=list(range(1,11))*2 # because each number can be used at most twice, if in the inner ring
    permutation_length=15
    possibilities = set(itertools.permutations(numbers,permutation_length))
    maxRingVal=0
    for i in possibilities:
        if isValid5Ring(i):
            ringVal = concatRing(i)
            logging.debug(f'{sum(i[0:3])}: {ringVal}')
            if ringVal > maxRingVal:
                maxRingVal = ringVal
    logging.debug(f'Max Ring Value: {maxRingVal}')  
    return maxRingVal

def concatRing(r):
    s=''
    for n in r:
        s += str(n)
    return int(s)
    
def isValid3Ring(ring):   
    if ring[1]!=ring[8]: return False
    if ring[2]!=ring[4]: return False
    if ring[5]!=ring[7]: return False

    if ring[0]>ring[3]: return False
    if ring[0]>ring[6]: return False
        
    total = sum(ring[0:3])
    total2 = sum(ring[3:6])
    total3 = sum(ring[6:9])
    if total==total2 ==total3:
        return True
    else:
        return False


def isValid5Ring(ring):   
    if ring[1]!=ring[14]: return False
    if ring[2]!=ring[4]: return False
    if ring[5]!=ring[7]: return False
    if ring[8]!=ring[10]: return False
    if ring[11]!=ring[13]: return False
    
    if ring[0]>ring[3]: return False
    if ring[0]>ring[6]: return False
    if ring[0]>ring[9]: return False
    if ring[0]>ring[12]: return False

    if ring[0] != 10 and ring[3]!=10 and ring[6]!=10 and ring[9]!=10 and ring[12]!=10: return False

    total = sum(ring[0:3])
    total2 = sum(ring[3:6])
    total3 = sum(ring[6:9])
    total4 = sum(ring[9:12])
    total5 = sum(ring[12:15])
    if total==total2 ==total3==total4==total5:
        return True
    else:
        return False
    
# observation: in a 5-gon made of 5 strings of 3 numbers, you need 10 numbers
# if the number 10 is in an outer most node, then the string that defines the ring will be 16 characters long
# if the number 10 is in an inner node, the defining string will be 17 characters long as the 10 will be used twice
# we are looking only for 16 digit ring definitions, and ring definitions start with the lowest external number
# and so our answer will not start with '10'

# This function calculates the answer and returns it
def solution():
    #implement solution to the problem here
    solution=ring3()
    solution=ring5()
    return solution

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    # logging.info('Solution = {}'.format(solution))
    # assert (solution == expectedAnswer)
    