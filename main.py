

def continued_fraction_sqrt(N):
    a0 = int(N**0.5)
    
    m = [0]
    d = [1]
    a = [a0]

    for i in range(1000):  # limit iterations to avoid infinite loops in our code
        m.append(d[-1] * a[-1] - m[-1])
        d.append((N - m[-1]**2) / d[-1])
        a.append(int((a0 + m[-1]) / d[-1]))

        # Check if sequence starts to repeat
        if a[-1] == 2 * a0:
            break

    return a0, a[1:]

N = 23
a0, coeffs = continued_fraction_sqrt(N)
print(f"Square root of {N} = [{a0}; {', '.join(map(str, coeffs))}]")

def sumcount(n):
  if n==2:
    return 1 # 1+1
  else:
    return sumcount(n-1)+1 

def partition_count(n):
    # memoization table, where dp[i] will store the number of ways to write i as the sum of integers
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]

while True:
  n = int(input("Enter a number: "))
  print(f"There are {partition_count(n)} ways to write {n} as the sum of positive integers.")
