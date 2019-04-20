# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of
# eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of
# queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next
# highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
#
# Hand	| 	Player 1        | 	Player 2	     | 	Winner
#       |                   |                    |
# 1	 	| 5H 5C 6S 7S KD    | 2C 3S 8S 8D TD     | Player 2
#       | Pair of Fives     | Pair of Eights     |
#       |                   |                    |
# 2	 	| 5D 8C 9S JS AC    | 2C 5C 7D 8S QH     | Player 1
#       | Highest card Ace  | Highest card Queen |
#       |                   |                    |
# 3	 	| 2D 9C AS AH AC    | 3D 6D 7D TD QD     | Player 2
#       | Three Aces        | Flush with Diamonds|
#       |                   |                    |
# 4	 	| 4D 6S 9H QH QC    | 3D 6D 7H QD QS     | Player 1
#       | Pair of Queens    | Pair of Queens     |
#       | Highest card Nine | Highest card Seven |
#       |                   |                    |
# 5	    | 2H 2D 4C 4D 4S    | 3C 3D 3S 9S 9D     | Player 1
#       | Full House        | Full House         |
#       | With Three Fours  | with Three Threes  |
#
#
#
#
# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?



# put the expected answer here
expectedAnswer=376

import logging, math, timeit, time, csv, collections, os, psutil
import platform, os, csv, collections

def cardValue(v):
    values = {
        '2':2,
        '3':3,
        '4':4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    return values[v]

def handValues(hand):
    return [cardValue(i[0]) for i in hand]

def handSuits(hand):
    return [i[1] for i in hand]

def isSameSuit(hand):
    x=handSuits(hand)
    if len(set(x))== 1: #len(x):
        return True
    else:
        return False

#convenience function to lookup keys with particular values
def reverse_lookup(d, v):
    results=[]
    for k, val in d.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if val == v:
            results.append(k)
    return sorted(results,reverse=True)


def rank(hand):
    hand=sorted(hand)
    values=sorted(handValues(hand),reverse=True)[::-1]
    sameSuit = isSameSuit(hand)
    if sameSuit:
        if sum(values)==(14+13+12+11+10):
            return ('Royal Flush', values)
        # 0 + 1 + 2 + 3 + 4 = 10 in total, so the value of a straight is the lowest value card * 5 plus 10
        # e.g. 3,4,5,6,7 = 25

        if values[0] + 4 == values[1] + 3 == values[2] + 2 == values[3] + 1 == values[4]:
            return ('Straight Flush', values)
    counter=collections.defaultdict(int)
    for v in values:
        counter[v]+=1
    mostfreq = max(counter.items(), key=lambda x: x[1])[1]
    if mostfreq==4:
        return ('Four of a kind', values,reverse_lookup(counter,4))
    if mostfreq==3 and len(counter.items())==2:
        return ('Full house', values,(reverse_lookup(counter,3),reverse_lookup(counter,2)))
    if sameSuit:
        return ('Flush', values,reverse_lookup(counter,1))
    if values[0]+4 == values[1]+3 == values[2]+2 == values[3] +1 == values[4]:
        return ('Straight',values,reverse_lookup(counter,1))
    if mostfreq==3:
        return ('Three of a kind', values,reverse_lookup(counter,3))
    if mostfreq==2 and len(counter.items())==3:
        return ('Two pairs', values,reverse_lookup(counter,2))
    if mostfreq==2:
        return ('One pair', values,(reverse_lookup(counter,2),max(reverse_lookup(counter,1))))
    return ('High card',values,reverse_lookup(counter,1))

ranks = {
    'High card':1,
    'One pair':2,
    'Two pairs':3,
    'Three of a kind':4,
    'Straight':5,
    'Flush':6,
    'Full house':7,
    'Four of a kind':8,
    'Straight Flush':9,
    'Royal Flush':10
}

def play(hand1, hand2):
    one = rank(hand1)
    two = rank(hand2)

    # compare named hands to do a simple coparison to see who wins
    if ranks[one[0]]>ranks[two[0]]:
        return True
    if ranks[two[0]]>ranks[one[0]]:
        return False

    if (one[0]!='High card'):
        logging.info('MATCHED HANDS: player one: {}, player two: {}'.format(hand1, hand2))
    # now if the ranks are the same, we need to see which scores higher

    if type(one[2] == list):
        if one[2][0] > two[2][0]:
            return True
        if two[2][0] > one[2][0]:
            return False
        else:
            if one[2][1] > two[2][1]:
                return True
            if two[2][1] > one[2][1]:
                return False

    # elif type(one[2])== tuple:  # because we could get a full house or a two pair
    #     pass


    scores1 = one[1]
    scores2 = two[1]
    for i,s in enumerate(scores1):
        if s>scores2[i]:
            return True
        if scores2[i]>s:
            return False
    return True


def solution():



    player1=[]
    player2=[]
    player1Wins=0
    player2Wins=0
    with open('p054_poker.txt', 'r') as f:
        reader = csv.reader(f, delimiter = ' ')
        rounds = list(reader)
        player1 = [i[0:5] for i in rounds]
        player2 = [i[5:] for i in rounds]
        logging.info('Playing {} rounds'.format(len(rounds)))


    for i in range(len(player1)):

        if play(player1[i],player2[i]):
            player1Wins+=1
            logging.info('ROUND {}: Player 1 {} beats Player 2 {} '.format(i+1,rank(player1[i]), rank(player2[i])))
        else:
            player2Wins+=1
            logging.info('ROUND {}: Player 1 {} loses Player 2 {} '.format(i+1,rank(player1[i]), rank(player2[i])))

    logging.info('Player 1 wins {} rounds, Player 2 wins {} rounds'.format(player1Wins,player2Wins))
    assert(player1Wins+player2Wins == len(rounds))

    return player1Wins


# Utility function for measuring the performance of solutions
processtime=0.0
walltime=0.0
def stopwatch():
    global walltime, processtime
    wt=time.time()
    ct=time.clock()
    wtElapsed=wt-walltime
    ctElapsed=ct-processtime
    walltime=wt
    processtime=ct
    return('Elapsed process time:{}s, Elapsed clock time:{}s'.format(ctElapsed,wtElapsed))

def getsysteminfo():
    p=platform.platform()+' ' +platform.processor()+' Python: '+platform.python_version()
    memory=psutil.virtual_memory()
    cpuc=psutil.cpu_count()
    cpup=psutil.cpu_count(logical=True)
    cpuf=psutil.cpu_freq()
    cput=psutil.cpu_times_percent(percpu=False)

    return 'Platform: {}, Memory: {} Physical CPUs: {}, Logical CPUs: {}, Frequency (MHz): {}, Utilisation: {}'.format\
        (p,memory,cpuc,cpup,cpuf,cput)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    stopwatch() #start timing
    solution = solution()
    timetaken=stopwatch() #stop timing
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))

