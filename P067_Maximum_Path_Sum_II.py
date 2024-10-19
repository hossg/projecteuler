# put the expected answer here
expectedAnswer = 7273

import logging, math, timeit, time, psutil, platform, os


def read_triangle_file(file_path):
    with open(file_path, 'r') as file:
        triangle = []
        for line in file:
            # Strip newline characters and split the line into numbers
            numbers = list(map(int, line.strip().split()))
            triangle.append(numbers)
    return triangle


# Reading the file '0067_triangle.txt' and printing the result
file_path = 'p067_triangle.txt'
triangle_data = read_triangle_file(file_path)


def solution():

    current_row = 98
    while current_row >= 0:
        for i in range(len(triangle_data[current_row])):

            triangle_data[current_row][
                i] = triangle_data[current_row][i] + max(
                    triangle_data[current_row + 1][i],
                    triangle_data[current_row + 1][i + 1])
        current_row -= 1


    solution = triangle_data[0][0]

    return solution


# Utility function for measuring the performance of solutions
processtime = 0.0
walltime = 0.0


def stopwatch():
    global walltime, processtime
    wt = time.time()
    ct = time.process_time()
    wtElapsed = wt - walltime
    ctElapsed = ct - processtime
    walltime = wt
    processtime = ct
    return ('Elapsed process time:{}s, Elapsed clock time:{}s'.format(
        ctElapsed, wtElapsed))


def getsysteminfo():
    p = platform.platform() + ' ' + platform.processor(
    ) + ' Python: ' + platform.python_version()
    memory = psutil.virtual_memory()
    cpuc = psutil.cpu_count()
    cpup = psutil.cpu_count(logical=True)
    cpuf = psutil.cpu_freq()
    cput = psutil.cpu_times_percent(percpu=False)

    return 'Platform: {}, Memory: {} Physical CPUs: {}, Logical CPUs: {}, Frequency (MHz): {}, Utilisation: {}'.format\
        (p,memory,cpuc,cpup,cpuf,cput)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging = logging.getLogger(os.path.basename(__file__))
    stopwatch()  #start timing
    solution = solution()
    timetaken = stopwatch()  #stop timing
    #assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))
