def continued_fraction_sqrt(N):
    a0 = int(N**0.5)

    m = [0]
    d = [1]
    a = [a0]

    for i in range(
            1000):  # limit iterations to avoid infinite loops in our code
        m.append(d[-1] * a[-1] - m[-1])
        d.append((N - m[-1]**2) / d[-1])
        a.append(int((a0 + m[-1]) / d[-1]))

        # Check if sequence starts to repeat
        if a[-1] == 2 * a0:
            break

    return a0, a[1:]


def continued_fraction_sqrt_as(N):
    a0, ai = continued_fraction_sqrt(N)
    a = [a0] + ai
    return a


def convergent(N, k):
    a0, ai = continued_fraction_sqrt(N)
    while k >= len(ai)-1:
        ai = ai * 2
    print(k, ai)
    pk = convergent_p(a0, ai, k)
    qk = convergent_q(a0, ai, k)
    return pk, qk


def convergent_p(a0, ai, k):
    if k == 0: p = a0
    elif k == 1: p = a0 * ai[0] + 1
    else:
        p = ai[k + 1] * convergent_p(a0, ai, k - 1) + convergent_p(
            a0, ai, k - 2)
    return p


def convergent_q(a0, ai, k):
    if k == 0: q = 1
    elif k == 1: q = ai[0]
    else:
        q = ai[k + 1] * convergent_q(a0, ai, k - 1) + convergent_q(
            a0, ai, k - 2)
    return q


N = 23
while True:
    N = int(input("Enter a number: "))
    convergents = []
    # print(convergent(N, 3))
    for k in range(7):
        pk, qk = convergent(N, k)
        convergents.append((pk, qk))
    a0, coeffs = continued_fraction_sqrt(N)
    print(f"Square root of {N} = [{a0}; {', '.join(map(str, coeffs))}]")
    print(f"convergents of {N} = {convergents}")


def sumcount(n):
    if n == 2:
        return 1  # 1+1
    else:
        return sumcount(n - 1) + 1


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
    print(
        f"There are {partition_count(n)} ways to write {n} as the sum of positive integers."
    )
