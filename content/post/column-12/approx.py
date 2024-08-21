import numpy as np

def EX_approx(m, n):
    # Fix a max. runtime that we consider. Let's take 2n
    s = 2*n
    # P[i][k] gives P(Y^(i) = k)
    P = np.zeros((s,s))
    Y = np.zeros(s)
    Y[1] = 1 / n
    P[1][0] = (n-1) / n
    P[1][1] = 1 / n
    for i in range(2,s):
        # Inner loop only until i, because the values can't be larger
        for k in range(i):
            Y[i] += (i-k) / n * P[i-1][k]
        if i-m >= 0:
            Y[i] *= P[i-1][i-m:].sum()
        for k in range(i):
            P[i][k] = P[i-1][k] * (1 - Y[i]) + P[i-1][k-1] * Y[i]
    
    return m + Y.sum()

print(EX_approx(20, 100))