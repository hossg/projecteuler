# put the expected answer here
expectedAnswer = 402

import logging, math, timeit, time, psutil, platform, os


def solution():

  # first calculate the lengths of all chains for numbers upto a million
  chain_max = 1000000
  chain_lengths = [0] * chain_max
  for i in range(chain_max):
    chain_lengths[i] = get_chain_length(i, chain_lengths)

  # and the solution is the number of these with length 60
  solution = (len([i for i, v in enumerate(chain_lengths) if v == 60]))
  assert solution == expectedAnswer
  return solution


#purely a performance hack
def precalculate_digit_factorials():
  digit_factorials = [math.factorial(i) for i in range(10)]
  return digit_factorials

digit_factorials = precalculate_digit_factorials()

# Get the sum of factorial of the digits
def sum_of_factorials(num):
  # return sum(math.factorial(int(digit)) for digit in str(num))
  return sum(digit_factorials[int(digit)] for digit in str(num))


# Get the chain for the number; not actually needed or used but convenient during development
def get_chain(num):
  seen = set()
  chain = []
  while num not in seen:
    seen.add(num)
    chain.append(num)
    num = sum_of_factorials(num)
  return chain


# get the length of a chain, re-using the pre-existing lengths of chains already provided
# and updating that list for future use
def get_chain_length(i, chain_lengths):
  seen = set()
  chain = []
  num = i
  chain_max = len(chain_lengths)
  while num not in seen:
    seen.add(num)
    chain.append(num)
    num = sum_of_factorials(num)
    if num < chain_max and chain_lengths[num] != 0:
      chain_lengths[i] = len(chain) + chain_lengths[num]
      return chain_lengths[i]
  chain_lengths[i] = len(chain)
  return chain_lengths[i]

processtime = 0.0
walltime = 0.0


def stopwatch():
  global walltime, processtime
  wt = time.time()
  ct = time.clock()
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
  logging.basicConfig(level=logging.INFO,
                      format='%(asctime)s %(levelname)s %(name)s %(message)s')
  logging = logging.getLogger(os.path.basename(__file__))
  stopwatch()  #start timing
  solution = solution()
  timetaken = stopwatch()  #stop timing
  #assert (solution == expectedAnswer)
  logging.info('Solution = {}'.format(solution))
  logging.info(timetaken)
  logging.info('System info: {}'.format(getsysteminfo()))
