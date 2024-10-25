# Put the problem description here, including a link to the problem on the website if available.

# Put the expected answer here
expectedAnswer=427337

import logging,os
import csv

def read_csv_to_array(filename):
    array = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Convert each row of strings to a list of integers
            int_row = [int(value) for value in row]
            array.append(int_row)
    return array


# This function calculates the answer and returns it
def solution():
    matrix = read_csv_to_array('p081_matrix.txt')
    logging.debug(f'read in matrix of {len(matrix[0])} by {len(matrix)}')

    # initialise the top row and the LHS column
    n=len(matrix)
    for i in range (1,n):
        matrix[0][i]+=matrix[0][i-1]
        matrix[i][0]+=matrix[i-1][0]

    for i in range(1,n):
        for j in range(1,n):
            matrix[i][j] += min(matrix[i-1][j],matrix[i][j-1])

    return matrix[n-1][n-1]




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    sol = solution()
    logging.info('Solution = {}'.format(sol))
    assert (sol == expectedAnswer)
    