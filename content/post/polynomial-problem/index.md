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

Formally, a valid path $\mathcal P$ with $n \in \N$ transitions is given by an initial polynomial index $t_0 \in I$, a list of polynomial indices $\mathbf t \in I^n$ and switching $x$-coordinates $\mathbf x \in \R^n$ such that $p_{t_{i-1}}(x_i) = p_{t_i}(x_i)$ for all $i = 1,\dots,n$. Set $x_0 \coloneqq 0$. The length of $\mathcal P$ is the sum of the arc lengths
$$
    \ell(\mathcal P) \coloneqq \sum_{i=0}^n \int_{x_i}^{x_{i+1}} \left\lvert p_{t_i}(t)\right\rvert \mathrm d t.
$$

Using this definition, the problem can be succinctly stated as finding $\argmin \ell(P)$.

# Solution
Well, I actually don't have a solution yet. But here is a starting point.

First off, this is a classic constrained optimization problem. We want to find a big tuple $(t_0,t_1,\dots,t_n,x_1,\dots,x_n)$ fulfilling some constraints. Notice how the size of the tuple depends on $n$, which we technically would also like to optimize over. For simplicity, let's fix $n$ and allow repetitions ($x_i = x_{i+1}$ for some of the $i$'s). That way, we can still find optimal solutions, provided $n$ is large enough.

## Dynamic Programming
In principle, this just a shortest path problem, so with some precomputation, we can reduce the polynomials to a graph and run a weighted shortest-path algorithm, such as Dijkstra's algorithm. So, what are the precomputations? The intersection points of the polynomials as well as the arc lengths between two such intersection points! More precisely, we'd need to do the following:

1. For each pair of polynomials, determine their intersection points by subtracting the lower-degree one from the other and finding all real roots of the resulting polynomial.
2. Next, we split each polynomial $p$ at all found intersection points as well as the origin and $\mathbb p$, in case $p$ runs through them. For each of the finite sections, compute the arc length and store the whole thing in a graph.
3. Run Dijkstra's algorithm on the resulting graph.

### Complexity analysis
Dijkstra's algorithm has a complexity of $\mathcal O((|V|+|E|)\log |V|)$. In our case, vertices are intersection points. In terms of edges, there is a trade-off between degree (of a vertex) and edges: When two polynomials intersect, that intersection point forms a vertex with two edges. If a third polynomial runs through that same point, we get another two (or one) edges, but one less vertex overall. But what is the number of intersection points exactly? In the worst case, $\sum_{i,j \in \binom{I}{2}} \min(\deg(p_i), \deg(p_j))$.

to be continued...

<!--In our case, vertices are intersection points of which there are at most $\frac{1}{2} \sum_{i \in I} \deg(p_i) + 2$ (where the $+2$ is because of the origin and the goal). In terms of edges, there is a trade-off between degree (of a vertex) and edges: When two polynomials intersect, that intersection point forms a vertex with two edges. If a third polynomial runs through that same point, we get another two (or one) edges, but one less vertex overall. Hence, we can have at most $\sum_{i\in I} \deg(p_i)$ edges.

What about preprocessing? Based on the steps outlined above, we would do $\binom{|I|}{2}$ root-finding steps. I am not familiar with the variety of root-finding algorithms, but according to MATLAB, it can be done for a $d$-degree polynomial by computing the eigenvalues of an $d \times d$ matrix, which in turn has a complexity of $d^3$. Phew, sounds inefficient. But let's see how far this can takes us. -->

### Implementation
to be continued...