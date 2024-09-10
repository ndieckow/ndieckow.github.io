import random
import numpy as np

def EX_approx(m, n):
    # Fix a max. runtime that we consider. Let's take 2n
    s = 8*n
    # P[i][k] gives P(Y^(i) = k)
    P = np.zeros((s,s))
    Y = np.zeros(s)
    Y[1] = 1 / n
    P[1][0] = (n-1) / n
    P[1][1] = 1 / n
    for i in range(2,s):
        # Inner loop only until i, because the values can't be larger
        for k in range(i):
            Y[i] += (i-k) / n * P[i-1][k] * (k > i-m)
        for k in range(i):
            p1 = (i-k) / n * (k > i-m)
            p2 = (i-(k-1)) / n * (k-1 > i-m)
            P[i][k] = P[i-1][k] * (1 - p1) + P[i-1][k-1] * p2
    
    return m + Y.sum()

def sample_m(m, n):
    assert m <= n
    S = set()
    it = 0
    while len(S) < m:
        S.add(random.randint(1,n))
        it += 1
    return S, it

import matplotlib.pyplot as plt

N = 1000
n = 10
its = []
it_approxs = []
for i in range(1,n+1):
    it_mean = 0
    for _ in range(N):
        _, it = sample_m(i, n)
        it_mean += it
    its.append(it_mean / N)

    it_approx = EX_approx(i, n)
    print(f"{i} | {it_approx:.2f}")
    it_approxs.append(it_approx)

plt.figure()
plt.scatter(range(1,n+1), its, label="True")
plt.scatter(range(1,n+1), it_approxs, label="Expected")
plt.legend()
plt.show()