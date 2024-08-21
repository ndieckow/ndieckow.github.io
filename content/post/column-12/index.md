---
title: 'Some Thoughts on Programming Pearls: Column 12'
date: 2024-08-21
draft: true
math: true
toc: true
author: Niklas
image: cover.jpg
tags:
    - programming
    - probability
    - math
categories:
    - Math
---

Let's say we are randomly sampling m numbers out of a set of n numbers, where $n \geq m$. We will randomly choose a number between $1$ and $n$ and add it to a set, until our set reaches a size of $m$. What is the expected number of draws required?

This question was inspired by Column 12 "A Sample Problem" from the book "Programming Pearls" by Jon Bentley.

Let's define a few random variables:
* $X$ is the number of iterations,
* $Y$ is the number of repeat draws; note that $Y = X - m$,
* Let $Y_i$ be $1$, if the $i$-th draw was a repeat draw and the current set size is at most $m$. Otherwise it is $0$. Note that $Y = \sum_{i=1}^\infty Y_i$,
* To add to the superscript confusion, let's also define partial sums $Y^{(i)} = \sum_{k=1}^{i} Y_k$

Our goal is to compute $\mathbb E[X] = m + \mathbb E[\sum_{k=1}^\infty Y_i] = m + \sum_{k=1}^\infty \mathbb E[Y_i]$.

The first observation is that the probability of $Y_i$ being $1$ depends on the values of $Y_k$ for $k < i$: This is because the probability of a repeat draw is $c/n$, where $c$ is the current size of our set, and, in a particular instance of our random experiment, $c$ corresponds to $i-Y^{(i-1)}$. Because we cannot make the probability of a random variable depend on another random variable directly, we make use of the *law of total probability*.

$$\mathbb E[Y_i] = P(Y_i = 1) = P(Y^{(i-1)} > 1-(i+m)) \sum_{k=0}^{i-1} \frac{i-k}{n} P(Y^{(i-1)} = k)$$
But also:
$$P(Y^{(i)} = k) = P(Y^{(i-1)} = k) P(Y_i = 0) + P(Y^{(i-1)} = k-1) P(Y_i = 1).$$

Intermediate step:
$$P(Y_i = 1 \mid Y^{(i-1)} = k) = \frac{i-k}{n} P(Y^{(i-1)} \geq i-m)$$

This dynamic programming formulation lends itself to a nice recursive algorithm that approximates $\mathbb E[X]$.

```python
import numpy as np

def EX_approx(m, n):
    # Fix a max. runtime that we consider. Let's take 2n
    s = 2*n
    # P[i][k] gives P(Y^(i) = k)
    P = np.zeros((s,s))
    Y = np.zeros(s)
    for i in range(s):
        # Inner loop only until i, because the values can't be larger
        for k in range(i):
            Y[i] += (i-k) / n * P[i-1][k]
        for k in range(i):
            P[i][k] = P[i-1][k] * (1 - Y[i]) + P[i-1][k-1] * Y[i]
```