# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for
# Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
# taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
# restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
# bytes. The user would keep the encrypted message and the encryption key in different locations, and without both
# "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
# If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt
# (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the
# plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original
# text.

# put the expected answer here
expectedAnswer=129448

import logging, math, timeit, time, psutil, platform, os
import itertools

def ints_to_string(ints):
    return ''.join([chr(c) for c in ints])

def string_to_ints(s):
    return [ord(c) for c in s]


def code_decode_ints(cipher, key):
    cyclable_key = itertools.cycle(key)  # make the key repeating so we don't run out of space
    xored = ''.join(chr(a ^ b) for (a,b) in zip(cipher,cyclable_key))
    return xored

# a simple function to check whether generated plaintext characters are valid English letters or punctuation.
def is_valid_plaintext_char(n):
    if (n >= 32 and n <= 122):
        return True
    else:
        return False

# our main job is to find the encryption key. we know it is 3 characters long, and each character is a lower-case
# letter.

def solution(): # an array of ints representing the ciphertext

    with open('p059_cipher.txt', 'r') as f:
        s=f.readline()
        cipher = [ int(x) for x in s.split(',')]


    key_characters = 'abcdefghijklmnopqrstuvwxyz'
    key_codes = string_to_ints(key_characters)

    possible_key_codes=[]
    possible_key_codes.append(key_codes.copy())
    possible_key_codes.append(key_codes.copy())
    possible_key_codes.append(key_codes.copy()) # 3 lists of possible characters

    for k in key_codes: # for each possible letter of the key
        for n in range (3): # for each position in the key
            for i in range(n,len(cipher),3): # we're going to check every 3rd character because we know the key is 3
                               # characters long
                if not is_valid_plaintext_char(k ^ cipher[i]):  # if the character doesn't map to a valid plaintext char
                    if k in possible_key_codes[n]:         # and if the character is still in the list of possibles
                        possible_key_codes[n].remove(k)    # then remove it from the list of possibles

    logging.debug('Possible key codes, (letters 1,2,3): {}'.format(possible_key_codes))

    # any combination of those codes could form the key, so let's test them all and see if any contain English
    for k in itertools.product(*possible_key_codes):
        logging.debug('Testing key: {}'.format(ints_to_string(k)))
        plaintext=code_decode_ints(cipher, k)
        if ' the ' in plaintext:
            logging.debug('Found key: {}'.format(ints_to_string(k)))
            logging.debug('Plaintext: {}'.format(plaintext))
            ints = string_to_ints(plaintext)
            sum_of_ints = sum(ints)
            solution = sum_of_ints
            break

    return solution


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

