# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


# 1 - 1
# 2 - (1,1), 2
# 5 - 5,  1 + 2*2's - each of which can have combo(2) options = 5 221 1121 11111

# 10 - 10 55 5221 51121 511111 221221


import logging

expectedAnswer=73682

coins=[1,2,5,10,20,50,100,200]

cents = 200
denominations = [200,100,50,20, 10, 5,2, 1]
names = {200:"2 pounds", 100:"1 pound", 50:"50p", 20: "20p", 10: "10p", 5 : "5p", 2:"2p", 1 : "1p"}

def combinations(c): # returns the number of ways a coin can be made of the coins smaller than it
    if c==1:
        return 1
    elif c==2:
        return 2
    else:
        combos = 0
        i = coins.index(c)
        cbelow = coins[i-1]
        # how many times does the coin below go into c?
        times = int(c/cbelow)
        combos = times*combinations(cbelow)
        remainder = c%cbelow
        if remainder != 0:
            combos += combinations(remainder)
        return combos-1 # to allow for the main coin itself!


def combos(x):
    ways = [0]*(x+1)        # somewhere to store the results for each answer we want, upto and including 1 beyond the range we need
    ways[0]=1               # initialize the process
    for coin in coins:
        for i in range (coin, x+1):
            ways[i]+=ways[i-coin]
    return ways[x]



def countWays(total,set=coins, size=len(coins)):
  if (total<0):
    return 0
  if (total==0):
    return 1
  if (size==1):
    return 1
  else:
    result = countWays(total,set,size-1)+countWays(total-set[size-1],set,size)
    # term 1 = the number of ways you can make this amount with 1 smaller coin
    # term 2 = the number of ways you can make the amount left over once you've used the largest coin
    return result



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging.info(countWays(1))
    logging.info(countWays(2))
    logging.info(countWays(5))
    logging.info(countWays(10))
    logging.info(countWays(200))

def solution():
    return countWays(200)