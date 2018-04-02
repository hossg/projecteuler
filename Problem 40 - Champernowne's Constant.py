# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


import logging, math

s='0.'
for i in range(1,1000000):
    s+=str(i)

def d(d):
    return s[d+1]

def solution():
    ds=[]
    for n in range(6):
        digit=d(int(math.pow(10,n)))
        ds.append(digit)
        logging.info('d{}={}'.format(n+1,digit))

    product=1
    for i in ds:
        product*=int(i)
    return product


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution=solution()
    assert (solution==210)
    logging.info('Solution = {}'.format(solution))

