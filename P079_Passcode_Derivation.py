# https://projecteuler.net/problem=79

# Put the expected answer here
expectedAnswer=73162890

import logging,os

def read_3_digit_strings(file_path):
    with open(file_path, 'r') as file:
        # Read lines and strip whitespace
        strings = [line.strip() for line in file if line.strip()]
    return strings


def passcode_match(passcode,digits):

    d=0
    for c in passcode:
        digit = digits[d]
        if c == digit:
            d+=1
        if d==3:
            return True
    return False

def passcode_match_all(passcode, all):
    for digits in all:
        if not passcode_match(passcode, digits):
            return False
    return True
# This function calculates the answer and returns it
def solution():

    file_path = 'p079_keylog.txt'
    three_digit_strings = read_3_digit_strings(file_path)
    found = False
    for passcode in range (100,100000000):
        if passcode_match_all(str(passcode), three_digit_strings):
            logging.debug(f'Found {passcode}')
            return passcode

    return 123456789

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    sol = solution()
    logging.info('Solution = {}'.format(sol))
    assert (sol == expectedAnswer)
    