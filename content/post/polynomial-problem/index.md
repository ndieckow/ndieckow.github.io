---
title: 'A Polynomial Problem'
date: 2025-04-15
tags:
    - math
categories:
    - Math
---

# Problem Formulation
Suppose you have a family of polynomials $(p_i)_{i \in I}$, where $I$ is a *finite* index set. At least one of them passes through the origin. Additionally, you are given a point $\mathbf p \in \R^2$. At least one of the polynomials passes through this point. 

The goal is to find the shortest path from the origin to $\mathbf p$ by only traversing the polynomial curves, where it is possible to switch from one polynomial to another at their intersection points. If no such path exists, you should be able to prove it.

Formally, a valid path $\mathcal P$ with $n \in \N$ transitions is given by an initial polynomial index $t_0 \in I$, a list of polynomial indices $\mathbf t \in I^n$ and switching $x$-coordinates $\mathbf x \in \R^n$ such that $p_{t_{i-1}}(x_i) = p_{t_i}(x_i)$ for all $i = 1,\dots,n$. Set $x_0 \coloneqq 0$. The length of $\mathcal P$ is the sum of the arc lengths,
$$
    \ell(\mathcal P) \coloneqq \sum_{i=0}^n \int_{x_i}^{x_{i+1}} \sqrt{1 + (p_{t_i}'(t))^2} \;\mathrm d t.
$$

Using this definition, the problem can be succinctly stated as finding $\argmin \ell(P)$.

# Solution
Well, I actually don't have a solution yet. But here is a starting point.

First off, this is a classic constrained optimization problem. We want to find a big tuple $(t_0,t_1,\dots,t_n,x_1,\dots,x_n)$ fulfilling some constraints. Notice how the size of the tuple depends on $n$, which we technically would also like to optimize over. For simplicity, let's fix $n$ and allow repetitions ($x_i = x_{i+1}$ for some of the $i$'s). That way, we can still find optimal solutions, provided $n$ is large enough.

## Dynamic Programming
In principle, this just a shortest path problem, so with some precomputation, we can reduce the polynomials to a graph and run a weighted shortest-path algorithm, such as Dijkstra's algorithm. So, what are the precomputations? The intersection points of the polynomials as well as the arc lengths between two such intersection points! More precisely, we'd need to do the following:

1. For each pair of polynomials, determine their intersection points by subtracting the lower-degree one from the other and finding all real roots of the resulting polynomial.
2. Next, we split each polynomial $p$ at all found intersection points as well as the origin and $\mathbf p$, in case $p$ runs through them. For each of the finite sections, compute the arc length and store the whole thing in a graph.
3. Run Dijkstra's algorithm on the resulting graph.

### Complexity analysis
Dijkstra's algorithm has a complexity of $\mathcal O((|V|+|E|)\log |V|)$. In our case, vertices are intersection points. In terms of edges, there is a trade-off between degree (of a vertex) and edges: When two polynomials intersect, that intersection point forms a vertex with two edges. If a third polynomial runs through that same point, we get another two (or one) edges, but one less vertex overall. In fact, one can quickly observe that the resulting graph must be planar. This implies that the edges are on the same order of the vertices.

Okay, but what *is* the number of vertices/intersections? In the worst case, all polynomials have the same degree $d$ and each pair of polynomials intersect at $d$ points, that are not shared with any other intersections. Then, we would have $\binom{|I|}{2} d = \mathcal O(d |I|^2)$ many intersections. If the degrees are not uniform, replace $d$ by the maximum degree.
A quadratic number of intersections can indeed occur in practice: Consider $m$ polynomials of degree 0 with different offsets, as well as another $m$ linear functions with near-infinite slope, such that they appear vertical, spaced apart in the $x$ dimension. Then, the intersections form a grid of size $m^2$.

Because root-finding with the companion matrix method takes $\mathcal O(d^3)$ steps, the overall worst-case complexity is therefore $\mathcal O(d^3 |I|^2 + d |I|^2 \log(d |I|^2)) = \mathcal O(d |I|^2(d^2 + \log d + \log |I|))$. For a fixed degree, we thus get $\mathcal O(|I|^2 \log |I|)$. Hence, the problem is in $P$.

### Implementation
For starters, I have implemented a little class for polynomials.
```python
from __future__ import annotations
from typing import Sequence, List

import numpy as np

class Polynomial:
    def __init__(self, coefs: Sequence):
        self.coefs = np.array(coefs)
        nonzero_idx = np.where(self.coefs != 0)[0]
        if len(nonzero_idx) == 0:
            self.d = 0
            self.coefs = np.array([0])
        else:
            self.d = nonzero_idx[-1]
            self.coefs = self.coefs[:self.d+1]
    
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        return np.power(x.reshape(-1,1), np.arange(self.d+1)) @ self.coefs

    def roots(self) -> List[float]:
        """Computes all real roots of the polynomial using the companion matrix method.
        This method first constructs the companion matrix C of the (normalized) polynomial
        and then computes the eigenvalues of C.

        Returns
        -------
        List[float]
            Real roots of the polynomial.
        """
        assert self.coefs[-1] != 0, "Highest degree may not be 0."
        if self.d == 0:
            return []
        coefs = self.coefs / self.coefs[-1] # Normalize the highest power
        C = np.zeros((self.d,self.d))
        C[1:,:-1] = np.eye(self.d-1)
        C[:,-1] = -coefs[:-1]
        try:
            eigs, _ = np.linalg.eig(C)
        except:
            return []
        return [x.real for x in eigs if x.imag == 0]

    def derivative(self) -> Polynomial:
        return Polynomial(self.coefs[1:])

    def __add__(self, o: Polynomial) -> Polynomial:
        max_deg = max(self.d, o.d)
        coefs = np.pad(self.coefs, (0, max_deg - self.d)) + np.pad(o.coefs, (0, max_deg - o.d))
        return Polynomial(coefs)
    
    def __neg__(self) -> Polynomial:
        return Polynomial(-self.coefs)
    
    def __sub__(self, o: Polynomial) -> Polynomial:
        max_deg = max(self.d, o.d)
        coefs = np.pad(self.coefs, (0, max_deg - self.d)) - np.pad(o.coefs, (0, max_deg - o.d))
        return Polynomial(coefs)
    
    def __eq__(self, o: Polynomial) -> bool:
        return np.allclose(self.coefs, o.coefs)

    def __repr__(self) -> str:
        return " + ".join([f"{c:.2f}x^{n}" for n,c in enumerate(self.coefs)]).replace("x^0", "").replace("x^1", "x")
```

In particular, the root computation is done by computing the eigenvalues of the [companion matrix](https://en.wikipedia.org/wiki/Companion_matrix) of $p$. I did not know about this before, it's pretty neat. Of course, we have to watch out for numerical instabilities.

## A Simpler Solution?
While the above solution is guaranteed to give us an optimal result, it has quite a high time complexity. I wonder how much worse a simple algorithm would be. In particular, I'm thinking about the following one:

> Draw a straight line from the origin to the target point $\mathbf p$. Now consider only the vertices that are connected to the faces that this line passes through, and run Dijkstra on those.

To analyze this method, two questions need to be answered:

1. How many vertices do we end up with? Can we safely say that it is of a smaller order (linear instead of quadratic in the number of polynomials)?
2. How much accuracy is lost, if any?

## Connections to Topology?
In a way, this is a topology problem. If we ignore the surrounding space of $\mathbb R^2$, and consider our space as just the union of all the polynomial curves, we are essentially asking for the shortest path from one point to another in this topological space. Like a [geodesic](https://en.wikipedia.org/wiki/Geodesic), except that our space is not a smooth manifold.